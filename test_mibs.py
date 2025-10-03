#!/usr/bin/env python3
"""
Simple MIB usage test - verifies MIBs can be used for OID resolution
"""

from pysnmp.smi import builder
from pathlib import Path
import sys

# Use the actual path where MIBs are
mib_dir = Path('compiled_mibs/cisco').absolute()
print(f"Looking for MIBs in: {mib_dir}\n")

# Verify directory exists and has files
if not mib_dir.exists():
    print(f"ERROR: Directory does not exist: {mib_dir}")
    sys.exit(1)

py_files = list(mib_dir.glob('*.py'))
print(f"Found {len(py_files)} .py files\n")

# Create MIB builder
mib_builder = builder.MibBuilder()
mib_builder.add_mib_sources(builder.DirMibSource(str(mib_dir)))

# Test loading some MIBs
test_mibs = ['CISCO-SMI', 'CISCO-TC', 'CISCO-CDP-MIB', 'IF-MIB', 'SNMPv2-MIB']

for mib in test_mibs:
    try:
        mib_builder.load_modules(mib)
        print(f"✓ {mib} loaded successfully")
    except Exception as e:
        print(f"✗ {mib} failed: {str(e)[:150]}")