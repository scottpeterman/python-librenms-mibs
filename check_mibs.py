#!/usr/bin/env python3
"""
MIB Validation Tool
Tests that compiled MIBs can be loaded by PySNMP.

Usage:
    python validate_mibs.py compiled_mibs/cisco
    python validate_mibs.py compiled_mibs/juniper
    python validate_mibs.py compiled_mibs/cisco --sample 10
"""

import argparse
import sys
from pathlib import Path
from pysnmp.smi import builder
import json
from datetime import datetime


class MibValidator:
    """Validates compiled MIBs using PySNMP."""

    def __init__(self, mib_dir: Path, verbose: bool = False):
        self.mib_dir = Path(mib_dir).absolute()
        self.verbose = verbose
        self.stats = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'errors': []
        }

    def find_compiled_mibs(self) -> list[str]:
        """Find all compiled .py MIB files and return their module names."""
        if not self.mib_dir.exists():
            print(f"ERROR: Directory does not exist: {self.mib_dir}")
            return []

        mibs = []
        for file_path in self.mib_dir.glob('*.py'):
            # Skip __init__.py and other non-MIB files
            if not file_path.name.startswith('_'):
                mibs.append(file_path.stem)  # Just the name without .py

        return sorted(mibs)

    def validate_mib(self, mib_builder: builder.MibBuilder, mib_name: str) -> tuple[bool, str]:
        """
        Validate a single MIB can be loaded by PySNMP.
        Returns (success: bool, error_message: str)
        """
        try:
            mib_builder.load_modules(mib_name)
            return True, "OK"
        except Exception as e:
            error_msg = str(e)
            # Truncate long errors
            if len(error_msg) > 150:
                error_msg = error_msg[:150] + "..."
            return False, error_msg

    def validate_all(self, sample_size: int = None) -> dict:
        """Validate all (or sample of) MIBs in the directory."""
        mib_names = self.find_compiled_mibs()

        if not mib_names:
            print(f"No compiled MIBs found in {self.mib_dir}")
            return self.stats

        # Sample if requested
        if sample_size and sample_size < len(mib_names):
            import random
            mib_names = sorted(random.sample(mib_names, sample_size))
            print(f"\nValidating random sample of {sample_size} MIBs")

        print(f"\nMIB Directory: {self.mib_dir}")
        print(f"Validating {len(mib_names)} MIBs...\n")

        self.stats['total'] = len(mib_names)

        # Create single MIB builder for all tests
        mib_builder = builder.MibBuilder()
        mib_builder.add_mib_sources(builder.DirMibSource(str(self.mib_dir)))

        for idx, mib_name in enumerate(mib_names, 1):
            prefix = f"[{idx}/{len(mib_names)}]"

            success, error = self.validate_mib(mib_builder, mib_name)

            if success:
                print(f"{prefix} ✓ {mib_name}")
                self.stats['passed'] += 1
            else:
                print(f"{prefix} ✗ {mib_name}: {error}")
                self.stats['failed'] += 1
                self.stats['errors'].append({
                    'mib': mib_name,
                    'error': error
                })

        return self.stats

    def print_summary(self):
        """Print validation summary."""
        print(f"\n{'=' * 70}")
        print("VALIDATION SUMMARY")
        print(f"{'=' * 70}")
        print(f"Total MIBs:  {self.stats['total']}")
        print(f"Passed:      {self.stats['passed']}")
        print(f"Failed:      {self.stats['failed']}")

        if self.stats['total'] > 0:
            success_rate = (self.stats['passed'] / self.stats['total']) * 100
            print(f"Success:     {success_rate:.1f}%")

        if self.stats['errors']:
            print(f"\n{'=' * 70}")
            print("ERRORS (first 20):")
            print(f"{'=' * 70}")
            for error in self.stats['errors'][:20]:
                print(f"  {error['mib']}: {error['error']}")

            remaining = len(self.stats['errors']) - 20
            if remaining > 0:
                print(f"  ... and {remaining} more errors")

        # Save report
        report_file = self.mib_dir / 'validation_report.json'
        try:
            with open(report_file, 'w') as f:
                json.dump({
                    'timestamp': datetime.now().isoformat(),
                    'directory': str(self.mib_dir),
                    'stats': self.stats
                }, f, indent=2)
            print(f"\nDetailed report: {report_file}")
        except Exception as e:
            print(f"Warning: Could not write report: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Validate compiled MIBs can be loaded by PySNMP',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate all Cisco MIBs
  %(prog)s compiled_mibs/cisco

  # Validate all Juniper MIBs
  %(prog)s compiled_mibs/juniper

  # Validate random sample of 50 MIBs
  %(prog)s compiled_mibs/cisco --sample 50
        """
    )

    parser.add_argument('mib_dir', type=str, help='Directory containing compiled MIBs')
    parser.add_argument('--sample', type=int, metavar='N', help='Validate random sample of N MIBs')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    mib_dir = Path(args.mib_dir)
    if not mib_dir.exists():
        print(f"ERROR: Directory does not exist: {mib_dir}")
        sys.exit(1)

    validator = MibValidator(mib_dir, args.verbose)

    try:
        validator.validate_all(sample_size=args.sample)
        validator.print_summary()

        if validator.stats['failed'] > 0:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        validator.print_summary()
        sys.exit(130)
    except Exception as e:
        print(f"\nERROR: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()