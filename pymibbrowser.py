#!/usr/bin/env python3
"""
PyQt6 MIB Browser
Browse and explore compiled SNMP MIBs with a graphical interface.

Requirements:
    pip install PyQt6 pysnmp
"""

import sys
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTreeWidget, QTreeWidgetItem, QTextEdit, QSplitter, QPushButton,
    QLabel, QLineEdit, QComboBox, QFileDialog, QMessageBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QHeaderView, QStatusBar
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon

from pysnmp.smi import builder, view, compiler
from pysnmp.proto import rfc1902


class MibLoaderThread(QThread):
    """Background thread for loading MIBs without blocking UI."""
    finished = pyqtSignal(object, str)  # mib_builder, error_message
    progress = pyqtSignal(str)  # status message

    def __init__(self, mib_paths, mib_names=None):
        super().__init__()
        self.mib_paths = mib_paths
        self.mib_names = mib_names

    def run(self):
        try:
            self.progress.emit("Initializing MIB builder...")
            mib_builder = builder.MibBuilder()

            # Add MIB sources
            for path in self.mib_paths:
                self.progress.emit(f"Adding source: {path}")
                mib_builder.add_mib_sources(builder.DirMibSource(str(path)))

            # Load specific MIBs or discover and load all
            if self.mib_names:
                for mib in self.mib_names:
                    self.progress.emit(f"Loading {mib}...")
                    mib_builder.loadModules(mib)
            else:
                # Discover all MIB files in the directories
                self.progress.emit("Discovering MIBs...")
                mib_files_to_load = []

                for path in self.mib_paths:
                    mib_path = Path(path)
                    if mib_path.exists():
                        for mib_file in mib_path.glob('*.py'):
                            if not mib_file.name.startswith('_'):
                                mib_name = mib_file.stem
                                if mib_name not in mib_files_to_load:
                                    mib_files_to_load.append(mib_name)

                self.progress.emit(f"Found {len(mib_files_to_load)} MIBs to load...")

                # Load all discovered MIBs
                loaded_count = 0
                failed_count = 0
                for idx, mib_name in enumerate(sorted(mib_files_to_load)):
                    try:
                        if idx % 5 == 0:  # Update progress every 5 MIBs
                            self.progress.emit(f"Loading MIBs... {idx}/{len(mib_files_to_load)}")
                        mib_builder.load_modules(mib_name)
                        loaded_count += 1
                    except Exception as e:
                        failed_count += 1
                        # Don't stop on individual failures
                        continue

                self.progress.emit(f"Loaded {loaded_count} MIBs ({failed_count} failed)")

            self.progress.emit("MIB loading complete!")
            self.finished.emit(mib_builder, "")

        except Exception as e:
            self.finished.emit(None, str(e))


class MibBrowser(QMainWindow):
    """Main MIB Browser window."""

    def __init__(self):
        super().__init__()
        self.mib_builder = None
        self.mib_view = None
        self.current_mib_paths = []

        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("SNMP MIB Browser")
        self.setGeometry(100, 100, 1600, 900)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(5, 5, 5, 5)

        # Top toolbar
        toolbar = self.create_toolbar()
        layout.addLayout(toolbar)

        # Main splitter (horizontal split)
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left panel - MIB tree
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)

        tree_label = QLabel("MIB Tree")
        tree_label.setStyleSheet("font-weight: bold; padding: 5px;")
        left_layout.addWidget(tree_label)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["OID / Name", "Type"])
        self.tree.setColumnWidth(0, 350)
        self.tree.itemClicked.connect(self.on_tree_item_clicked)
        self.tree.itemExpanded.connect(self.on_tree_item_expanded)
        left_layout.addWidget(self.tree)

        main_splitter.addWidget(left_panel)

        # Right panel - Details with tabs
        right_panel = QTabWidget()

        # Details tab
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setFont(QFont("Consolas", 9))
        right_panel.addTab(self.details_text, "Details")

        # Properties table tab
        self.properties_table = QTableWidget()
        self.properties_table.setColumnCount(2)
        self.properties_table.setHorizontalHeaderLabels(["Property", "Value"])
        header = self.properties_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        right_panel.addTab(self.properties_table, "Properties")

        # Error log tab
        self.error_log = QTextEdit()
        self.error_log.setReadOnly(True)
        self.error_log.setFont(QFont("Consolas", 9))
        right_panel.addTab(self.error_log, "Error Log")

        main_splitter.addWidget(right_panel)
        main_splitter.setSizes([500, 1100])

        layout.addWidget(main_splitter)

        # Status bar at bottom
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def create_toolbar(self):
        """Create the top toolbar."""
        toolbar = QHBoxLayout()
        toolbar.setSpacing(10)

        # Load MIB directory button
        self.load_btn = QPushButton("Load MIB Directory")
        self.load_btn.clicked.connect(self.load_mib_directory)
        self.load_btn.setMinimumWidth(150)
        toolbar.addWidget(self.load_btn)

        # Current path display
        self.path_label = QLabel("No directory loaded")
        self.path_label.setStyleSheet("color: gray; font-style: italic;")
        toolbar.addWidget(self.path_label)

        toolbar.addStretch()

        # Load specific MIB
        toolbar.addWidget(QLabel("Load MIB:"))
        self.mib_input = QLineEdit()
        self.mib_input.setPlaceholderText("e.g., CISCO-MEMORY-POOL-MIB")
        self.mib_input.setMinimumWidth(250)
        self.mib_input.returnPressed.connect(self.load_specific_mib)
        toolbar.addWidget(self.mib_input)

        self.load_mib_btn = QPushButton("Load")
        self.load_mib_btn.clicked.connect(self.load_specific_mib)
        toolbar.addWidget(self.load_mib_btn)

        # Search
        toolbar.addWidget(QLabel("Search:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search OIDs/names...")
        self.search_input.setMinimumWidth(200)
        self.search_input.textChanged.connect(self.on_search)
        toolbar.addWidget(self.search_input)

        # Clear button
        clear_btn = QPushButton("Clear Search")
        clear_btn.clicked.connect(lambda: self.search_input.clear())
        toolbar.addWidget(clear_btn)

        return toolbar

    def log_error(self, message):
        """Add error message to error log."""
        self.error_log.append(f"[ERROR] {message}\n")

    def log_info(self, message):
        """Add info message to error log."""
        self.error_log.append(f"[INFO] {message}\n")

    def load_mib_directory(self):
        """Load MIB directory dialog."""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Compiled MIB Directory",
            str(Path.home())
        )

        if directory:
            self.current_mib_paths = [Path(directory)]
            self.path_label.setText(str(directory))
            self.path_label.setStyleSheet("color: black;")
            self.log_info(f"Loading MIB directory: {directory}")
            self.start_mib_loading()

    def load_specific_mib(self):
        """Load a specific MIB by name."""
        mib_name = self.mib_input.text().strip()
        if not mib_name:
            return

        if not self.current_mib_paths:
            QMessageBox.warning(
                self,
                "No MIB Path",
                "Please load a MIB directory first."
            )
            return

        self.log_info(f"Loading specific MIB: {mib_name}")
        self.start_mib_loading(mib_names=[mib_name])

    def start_mib_loading(self, mib_names=None):
        """Start loading MIBs in background thread."""
        self.status_bar.showMessage("Loading MIBs...")
        self.load_btn.setEnabled(False)
        self.load_mib_btn.setEnabled(False)

        self.loader_thread = MibLoaderThread(self.current_mib_paths, mib_names)
        self.loader_thread.progress.connect(self.on_load_progress)
        self.loader_thread.finished.connect(self.on_load_finished)
        self.loader_thread.start()

    def on_load_progress(self, message):
        """Update progress during MIB loading."""
        self.status_bar.showMessage(message)

    def on_load_finished(self, mib_builder, error):
        """Handle MIB loading completion."""
        self.load_btn.setEnabled(True)
        self.load_mib_btn.setEnabled(True)

        if error:
            self.status_bar.showMessage(f"Error loading MIBs")
            self.log_error(f"MIB load error: {error}")
            QMessageBox.critical(
                self,
                "MIB Load Error",
                f"Failed to load MIBs:\n\n{error}\n\nCheck the Error Log tab for details."
            )
            return

        self.mib_builder = mib_builder
        self.mib_view = view.MibViewController(self.mib_builder)

        self.status_bar.showMessage("MIBs loaded successfully")
        self.log_info("MIB loading successful")
        self.populate_tree()

    def populate_tree(self):
        """Populate the tree with loaded MIB objects."""
        if not self.mib_builder:
            return

        self.tree.clear()
        self.status_bar.showMessage("Building MIB tree...")
        QApplication.processEvents()

        # Get all loaded modules
        mib_symbols = self.mib_builder.mibSymbols

        # Create root nodes for each MIB module
        module_items = {}
        for module_name in sorted(mib_symbols.keys()):
            if module_name in ('SNMPv2-SMI', 'SNMPv2-TC', 'SNMPv2-CONF'):
                continue  # Skip base modules in tree

            root_item = QTreeWidgetItem(self.tree, [module_name, "MODULE"])
            root_item.setData(0, Qt.ItemDataRole.UserRole, {
                'type': 'module',
                'name': module_name
            })
            module_items[module_name] = root_item

            # Add placeholder for lazy loading
            QTreeWidgetItem(root_item, ["Loading...", ""])

        self.tree.expandToDepth(0)
        self.status_bar.showMessage(f"Loaded {len(module_items)} MIB modules")
        self.log_info(f"Tree populated with {len(module_items)} modules")

    def on_tree_item_expanded(self, item):
        """Lazy load tree children when expanded."""
        # Check if this is first expansion (has placeholder)
        if item.childCount() == 1:
            child = item.child(0)
            if child.text(0) == "Loading...":
                self.populate_tree_children(item)

    def populate_tree_children(self, parent_item):
        """Populate children of a tree item."""
        parent_item.takeChildren()  # Remove placeholder

        data = parent_item.data(0, Qt.ItemDataRole.UserRole)
        if not data:
            return

        if data['type'] == 'module':
            # Load all symbols from this module
            module_name = data['name']
            module_symbols = self.mib_builder.mibSymbols.get(module_name, {})

            symbol_count = 0
            for symbol_name, symbol_obj in sorted(module_symbols.items()):
                if symbol_name.startswith('_'):
                    continue

                try:
                    # Determine symbol type
                    symbol_type = self.get_symbol_type(symbol_obj)

                    item = QTreeWidgetItem(parent_item, [symbol_name, symbol_type])
                    item.setData(0, Qt.ItemDataRole.UserRole, {
                        'type': 'symbol',
                        'module': module_name,
                        'name': symbol_name,
                        'object': symbol_obj
                    })

                    # Add OID if available
                    try:
                        oid = self.mib_view.get_node_name(
                            self.mib_view.get_node_location((module_name, symbol_name))
                        )
                        if oid and oid[0]:
                            oid_str = '.'.join(map(str, oid[0]))
                            item.setText(0, f"{symbol_name} [{oid_str}]")
                    except:
                        pass

                    symbol_count += 1

                except Exception as e:
                    self.log_error(f"Error loading symbol {symbol_name} from {module_name}: {e}")

            self.log_info(f"Loaded {symbol_count} symbols from {module_name}")

    def get_symbol_type(self, symbol_obj):
        """Determine the type of a MIB symbol."""
        obj_str = str(type(symbol_obj).__name__)

        if 'ObjectType' in obj_str:
            return "OBJECT"
        elif 'ObjectIdentity' in obj_str:
            return "OID"
        elif 'ModuleIdentity' in obj_str:
            return "MODULE-IDENTITY"
        elif 'NotificationType' in obj_str:
            return "NOTIFICATION"
        elif 'TextualConvention' in obj_str:
            return "TC"
        elif 'MibTableColumn' in obj_str:
            return "MibTableColumn"
        elif 'MibTable' in obj_str:
            return "MibTable"
        else:
            return obj_str

    def on_tree_item_clicked(self, item, column):
        """Handle tree item click."""
        data = item.data(0, Qt.ItemDataRole.UserRole)
        if not data:
            return

        if data['type'] == 'symbol':
            self.display_symbol_details(data)
        elif data['type'] == 'module':
            self.display_module_details(data)

    def display_module_details(self, data):
        """Display details of a MIB module."""
        module_name = data['name']

        details = []
        details.append(f"Module: {module_name}")
        details.append(f"Type: MIB Module")
        details.append("")

        # Count symbols
        module_symbols = self.mib_builder.mibSymbols.get(module_name, {})
        symbol_count = len([s for s in module_symbols.keys() if not s.startswith('_')])
        details.append(f"Symbols: {symbol_count}")

        self.details_text.setText('\n'.join(details))
        self.properties_table.setRowCount(0)

    def display_symbol_details(self, data):
        """Display details of a MIB symbol."""
        module = data['module']
        name = data['name']
        obj = data['object']

        # Build details text
        details = []
        details.append(f"Module: {module}")
        details.append(f"Name: {name}")
        details.append(f"Type: {self.get_symbol_type(obj)}")
        details.append("")

        # Get OID
        oid_found = False

        # Try to get OID from object's name attribute first
        if hasattr(obj, 'name') and obj.name:
            try:
                oid_tuple = obj.name
                if isinstance(oid_tuple, tuple) and len(oid_tuple) > 0:
                    oid_str = '.'.join(map(str, oid_tuple))
                    details.append(f"OID: {oid_str}")
                    details.append(f"Numeric OID: {oid_tuple}")
                    oid_found = True
            except:
                pass

        # Fall back to MibViewController if name attribute didn't work
        if not oid_found:
            try:
                oid_tuple = self.mib_view.get_node_location((module, name))
                if oid_tuple:
                    oid_str = '.'.join(map(str, oid_tuple))
                    details.append(f"OID: {oid_str}")
                    details.append(f"Numeric OID: {oid_tuple}")
                    oid_found = True
            except Exception as e:
                # Log to error tab for debugging
                self.log_error(f"Could not resolve OID for {module}::{name}: {str(e)[:200]}")

        if not oid_found:
            details.append("OID: Not resolvable")

        details.append("")

        # Get object attributes
        details.append("Attributes:")
        for attr in sorted(dir(obj)):
            if not attr.startswith('_') and attr not in ['clone', 'prettyPrint']:
                try:
                    value = getattr(obj, attr)
                    if not callable(value):
                        value_str = str(value)
                        if len(value_str) > 100:
                            value_str = value_str[:100] + "..."
                        details.append(f"  {attr}: {value_str}")
                except:
                    pass

        self.details_text.setText('\n'.join(details))

        # Populate properties table
        self.populate_properties_table(obj)

    def populate_properties_table(self, obj):
        """Populate the properties table."""
        self.properties_table.setRowCount(0)

        properties = []

        # Common properties
        prop_names = ['syntax', 'units', 'maxAccess', 'status', 'description',
                      'reference', 'defVal', 'augmention', 'index']

        for prop in prop_names:
            if hasattr(obj, prop):
                try:
                    value = getattr(obj, prop)
                    # Check if value is not None and not an empty object
                    if value is not None:
                        value_str = str(value)
                        # Only add if there's actual content
                        if value_str and value_str.strip():
                            properties.append((prop, value_str))
                except Exception as e:
                    # Skip properties that can't be accessed
                    continue

        self.properties_table.setRowCount(len(properties))
        for i, (key, value) in enumerate(properties):
            key_item = QTableWidgetItem(key)
            value_item = QTableWidgetItem(value)
            value_item.setTextAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            self.properties_table.setItem(i, 0, key_item)
            self.properties_table.setItem(i, 1, value_item)

        self.properties_table.resizeRowsToContents()

    def on_search(self, text):
        """Filter tree based on search text."""
        if not text:
            # Show all items
            iterator = QTreeWidgetItemIterator(self.tree)
            while iterator.value():
                iterator.value().setHidden(False)
                iterator += 1
            self.status_bar.showMessage("Search cleared")
            return

        text = text.lower()
        match_count = 0

        # Hide/show items based on match
        iterator = QTreeWidgetItemIterator(self.tree)
        while iterator.value():
            item = iterator.value()
            item_text = item.text(0).lower()
            matches = text in item_text

            # If this is a child item that matches, show parent too
            if matches and item.parent():
                item.parent().setHidden(False)
                match_count += 1

            item.setHidden(not matches)
            iterator += 1

        self.status_bar.showMessage(f"Found {match_count} matches for '{text}'")


def main():
    """Run the MIB Browser application."""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern look

    browser = MibBrowser()
    browser.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()