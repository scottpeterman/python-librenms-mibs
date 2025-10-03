#!/usr/bin/env python3
"""
Batch MIB Compiler
Compiles multiple vendor MIB directories and optionally validates them.

Usage:
    python batch_compile_mibs.py --source /path/to/librenms/mibs --output ./compiled_mibs
    python batch_compile_mibs.py --source ./mibs --output ./compiled_mibs --validate
    python batch_compile_mibs.py --source ./mibs --output ./compiled_mibs --vendors cisco,juniper,arista
"""

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import json
import shutil


class BatchMibCompiler:
    """Batch compile and organize MIBs from multiple vendors."""

    def __init__(self, source_dir: Path, output_dir: Path, validate: bool = False,
                 offline: bool = False, verbose: bool = False):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.validate = validate
        self.offline = offline
        self.verbose = verbose
        self.results = {}

    def get_vendors(self, vendor_list: list = None) -> list:
        """Get list of vendor directories to compile."""
        if vendor_list:
            vendors = []
            for vendor in vendor_list:
                vendor_path = self.source_dir / vendor
                if vendor_path.exists() and vendor_path.is_dir():
                    vendors.append(vendor)
                else:
                    print(f"Warning: Vendor directory not found: {vendor}")
            return vendors

        # Auto-discover all vendor directories
        vendors = []
        for item in self.source_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                vendors.append(item.name)
        return sorted(vendors)

    def compile_vendor(self, vendor: str) -> dict:
        """Compile MIBs for a single vendor."""
        print(f"\n{'=' * 80}")
        print(f"Processing vendor: {vendor}")
        print(f"{'=' * 80}")

        vendor_source = self.source_dir / vendor
        vendor_output = self.output_dir / vendor
        temp_output = self.output_dir  # Compile to root first

        # Create vendor directory first
        vendor_output.mkdir(parents=True, exist_ok=True)

        # Build compilation command
        cmd = [
            sys.executable,
            'lnmsc.py',
            str(self.source_dir),
            '--vendor', vendor,
            '-o', str(temp_output)
        ]

        if self.offline:
            cmd.append('--offline')

        if self.verbose:
            cmd.append('-v')

        # Run compilation
        start_time = datetime.now()
        try:
            result = subprocess.run(cmd, capture_output=False, text=True)
            compile_success = result.returncode == 0
        except Exception as e:
            print(f"Error running compiler: {e}")
            return {
                'vendor': vendor,
                'success': False,
                'error': str(e)
            }

        compile_time = (datetime.now() - start_time).total_seconds()

        # Move files immediately after compilation
        moved_count = 0
        skipped_dirs = {'__pycache__'}

        try:
            print(f"\nMoving files to {vendor_output}...")

            # Move all .py files (but not directories or other vendors' folders)
            for item in temp_output.iterdir():
                # Skip directories (other vendor folders, __pycache__, etc)
                if item.is_dir():
                    continue

                # Skip non-Python files except JSON reports
                if item.suffix not in ['.py', '.json']:
                    continue

                # Move to vendor directory
                dest = vendor_output / item.name
                if dest.exists():
                    dest.unlink()  # Overwrite existing

                shutil.move(str(item), str(dest))
                moved_count += 1

            print(f"Moved {moved_count} files to {vendor_output}")

        except Exception as e:
            print(f"Error moving files: {e}")

        # Read compilation stats
        stats = {}
        report_path = vendor_output / 'compilation_report.json'
        if report_path.exists():
            try:
                with open(report_path, 'r') as f:
                    report = json.load(f)
                    stats = report.get('stats', {})
            except:
                pass

        result = {
            'vendor': vendor,
            'success': compile_success,
            'compile_time': compile_time,
            'files_moved': moved_count,
            'stats': stats,
            'output_dir': str(vendor_output)
        }

        # Validate if requested
        if self.validate and compile_success:
            result['validation'] = self.validate_vendor(vendor_output)

        self.results[vendor] = result
        return result

    def validate_vendor(self, vendor_dir: Path) -> dict:
        """Validate compiled MIBs for a vendor."""
        print(f"\n--- Validating {vendor_dir.name} ---")

        cmd = [
            sys.executable,
            'check_mibs.py',
            str(vendor_dir)
        ]

        if self.verbose:
            cmd.append('-v')

        start_time = datetime.now()
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            validate_success = result.returncode == 0
            validation_time = (datetime.now() - start_time).total_seconds()

            # Read validation report
            report_path = vendor_dir / 'validation_report.json'
            if report_path.exists():
                with open(report_path, 'r') as f:
                    validation_stats = json.load(f).get('stats', {})
            else:
                validation_stats = {}

            return {
                'success': validate_success,
                'time': validation_time,
                'stats': validation_stats
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def compile_all(self, vendors: list) -> dict:
        """Compile all specified vendors."""
        print(f"\n{'=' * 80}")
        print(f"Batch MIB Compilation")
        print(f"{'=' * 80}")
        print(f"Source: {self.source_dir}")
        print(f"Output: {self.output_dir}")
        print(f"Vendors: {len(vendors)}")
        print(f"Validate: {self.validate}")
        print(f"{'=' * 80}\n")

        overall_start = datetime.now()

        for idx, vendor in enumerate(vendors, 1):
            print(f"\n[{idx}/{len(vendors)}] {vendor}")
            self.compile_vendor(vendor)

        overall_time = (datetime.now() - overall_start).total_seconds()

        # Generate summary report
        self.print_summary(overall_time)
        self.save_batch_report(overall_time)

        return self.results

    def print_summary(self, total_time: float):
        """Print compilation summary."""
        print(f"\n\n{'=' * 80}")
        print("BATCH COMPILATION SUMMARY")
        print(f"{'=' * 80}")
        print(f"Total Time: {total_time:.1f} seconds ({total_time / 60:.1f} minutes)")
        print(f"Vendors Processed: {len(self.results)}")
        print(f"{'=' * 80}\n")

        # Per-vendor summary
        total_compiled = 0
        total_failed = 0

        print(f"{'Vendor':<20} {'Compiled':<10} {'Failed':<10} {'Time':<10} {'Status'}")
        print("-" * 80)

        for vendor, result in sorted(self.results.items()):
            stats = result.get('stats', {})
            compiled = stats.get('compiled', 0)
            failed = stats.get('failed', 0)
            time = result.get('compile_time', 0)
            status = '✓' if result.get('success') else '✗'

            total_compiled += compiled
            total_failed += failed

            print(f"{vendor:<20} {compiled:<10} {failed:<10} {time:<10.1f} {status}")

            # Add validation info if available
            if 'validation' in result:
                val_stats = result['validation'].get('stats', {})
                val_passed = val_stats.get('passed', 0)
                val_failed = val_stats.get('failed', 0)
                val_status = '✓' if result['validation'].get('success') else '✗'
                print(f"  └─ Validation: {val_passed} passed, {val_failed} failed {val_status}")

        print("-" * 80)
        print(f"{'TOTAL':<20} {total_compiled:<10} {total_failed:<10}")
        print(f"\nOutput directory: {self.output_dir.absolute()}")

    def save_batch_report(self, total_time: float):
        """Save batch compilation report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'source_dir': str(self.source_dir),
            'output_dir': str(self.output_dir),
            'total_time': total_time,
            'validate': self.validate,
            'vendors': self.results
        }

        report_file = self.output_dir / 'batch_compilation_report.json'
        try:
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"\nBatch report saved: {report_file}")
        except Exception as e:
            print(f"Warning: Could not save batch report: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Batch compile MIBs from multiple vendors',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Compile all vendors
  %(prog)s --source /path/to/librenms/mibs --output ./compiled_mibs

  # Compile specific vendors
  %(prog)s --source ./mibs --output ./compiled_mibs --vendors cisco,juniper,arista

  # Compile and validate
  %(prog)s --source ./mibs --output ./compiled_mibs --validate

  # Offline mode with verbose output
  %(prog)s --source ./mibs --output ./compiled_mibs --offline -v
        """
    )

    parser.add_argument('--source', '-s', type=str, required=True,
                        help='Source directory containing vendor MIB folders')
    parser.add_argument('--output', '-o', type=str, required=True,
                        help='Output directory for compiled MIBs')
    parser.add_argument('--vendors', type=str,
                        help='Comma-separated list of vendors to compile (default: all)')
    parser.add_argument('--validate', action='store_true',
                        help='Validate MIBs after compilation')
    parser.add_argument('--offline', action='store_true',
                        help='Do not use network fallbacks')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    source_dir = Path(args.source)
    if not source_dir.exists():
        print(f"ERROR: Source directory does not exist: {source_dir}")
        sys.exit(1)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parse vendor list
    vendor_list = None
    if args.vendors:
        vendor_list = [v.strip() for v in args.vendors.split(',')]

    # Run batch compilation
    compiler = BatchMibCompiler(
        source_dir,
        output_dir,
        validate=args.validate,
        offline=args.offline,
        verbose=args.verbose
    )

    try:
        vendors = compiler.get_vendors(vendor_list)
        if not vendors:
            print("ERROR: No vendor directories found")
            sys.exit(1)

        compiler.compile_all(vendors)

        # Exit with error if any compilations failed
        if any(not r.get('success', False) for r in compiler.results.values()):
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        compiler.print_summary(0)
        sys.exit(130)
    except Exception as e:
        print(f"\nERROR: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()