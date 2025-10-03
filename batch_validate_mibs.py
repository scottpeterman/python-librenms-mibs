#!/usr/bin/env python3
"""
Batch MIB Validator
Validates all compiled MIB directories and generates comprehensive reports.

Usage:
    python batch_validate_mibs.py --input ./compiled_mibs
    python batch_validate_mibs.py --input ./compiled_mibs --output validation_summary.json
"""

import argparse
import sys
from pathlib import Path
from pysnmp.smi import builder
import json
from datetime import datetime
from collections import defaultdict


class BatchMibValidator:
    """Validates compiled MIBs across multiple vendor directories."""

    def __init__(self, input_dir: Path, verbose: bool = False):
        self.input_dir = Path(input_dir).absolute()
        self.verbose = verbose
        self.vendor_results = {}
        self.overall_stats = {
            'total_vendors': 0,
            'total_mibs': 0,
            'total_passed': 0,
            'total_failed': 0,
            'vendors_100_percent': 0,
            'vendors_90_percent_plus': 0,
            'vendors_with_failures': 0
        }

    def find_vendor_directories(self) -> list[Path]:
        """Find all vendor subdirectories."""
        vendors = []
        if not self.input_dir.exists():
            print(f"ERROR: Directory does not exist: {self.input_dir}")
            return vendors

        for item in self.input_dir.iterdir():
            if item.is_dir() and not item.name.startswith('_'):
                # Check if it has .py files
                if any(item.glob('*.py')):
                    vendors.append(item)

        return sorted(vendors)

    def find_compiled_mibs(self, vendor_dir: Path) -> list[str]:
        """Find all compiled .py MIB files and return their module names."""
        mibs = []
        for file_path in vendor_dir.glob('*.py'):
            if not file_path.name.startswith('_'):
                mibs.append(file_path.stem)
        return sorted(mibs)

    def validate_vendor(self, vendor_dir: Path) -> dict:
        """Validate all MIBs for a single vendor."""
        vendor_name = vendor_dir.name

        if self.verbose:
            print(f"\nValidating {vendor_name}...")
        else:
            print(f"Validating {vendor_name}...", end=' ', flush=True)

        mib_names = self.find_compiled_mibs(vendor_dir)

        if not mib_names:
            print("no MIBs found")
            return {
                'vendor': vendor_name,
                'total': 0,
                'passed': 0,
                'failed': 0,
                'errors': []
            }

        # Create MIB builder for this vendor
        mib_builder = builder.MibBuilder()
        mib_builder.add_mib_sources(builder.DirMibSource(str(vendor_dir)))

        passed = 0
        failed = 0
        errors = []

        for mib_name in mib_names:
            try:
                mib_builder.load_modules(mib_name)
                passed += 1
                if self.verbose:
                    print(f"  ✓ {mib_name}")
            except Exception as e:
                failed += 1
                error_msg = str(e)
                if len(error_msg) > 100:
                    error_msg = error_msg[:100] + "..."
                errors.append({
                    'mib': mib_name,
                    'error': error_msg
                })
                if self.verbose:
                    print(f"  ✗ {mib_name}: {error_msg}")

        success_rate = (passed / len(mib_names) * 100) if mib_names else 0

        if not self.verbose:
            print(f"{passed}/{len(mib_names)} ({success_rate:.1f}%)")

        return {
            'vendor': vendor_name,
            'total': len(mib_names),
            'passed': passed,
            'failed': failed,
            'success_rate': success_rate,
            'errors': errors
        }

    def validate_all(self) -> dict:
        """Validate all vendor directories."""
        print(f"\n{'=' * 80}")
        print("Batch MIB Validation")
        print(f"{'=' * 80}")
        print(f"Input Directory: {self.input_dir}\n")

        vendors = self.find_vendor_directories()

        if not vendors:
            print("No vendor directories found")
            return self.vendor_results

        print(f"Found {len(vendors)} vendor directories\n")
        self.overall_stats['total_vendors'] = len(vendors)

        # Validate each vendor
        for idx, vendor_dir in enumerate(vendors, 1):
            result = self.validate_vendor(vendor_dir)
            self.vendor_results[result['vendor']] = result

            # Update overall stats
            self.overall_stats['total_mibs'] += result['total']
            self.overall_stats['total_passed'] += result['passed']
            self.overall_stats['total_failed'] += result['failed']

            if result['success_rate'] == 100.0:
                self.overall_stats['vendors_100_percent'] += 1
            elif result['success_rate'] >= 90.0:
                self.overall_stats['vendors_90_percent_plus'] += 1

            if result['failed'] > 0:
                self.overall_stats['vendors_with_failures'] += 1

        return self.vendor_results

    def print_summary(self):
        """Print validation summary."""
        print(f"\n{'=' * 80}")
        print("VALIDATION SUMMARY")
        print(f"{'=' * 80}\n")

        # Overall statistics
        print("Overall Statistics:")
        print(f"  Total Vendors:        {self.overall_stats['total_vendors']}")
        print(f"  Total MIBs:           {self.overall_stats['total_mibs']}")
        print(f"  Total Passed:         {self.overall_stats['total_passed']}")
        print(f"  Total Failed:         {self.overall_stats['total_failed']}")

        overall_success = 0
        if self.overall_stats['total_mibs'] > 0:
            overall_success = (self.overall_stats['total_passed'] /
                               self.overall_stats['total_mibs'] * 100)
        print(f"  Overall Success Rate: {overall_success:.2f}%")

        print(f"\nVendor Performance:")
        print(f"  100% Success:         {self.overall_stats['vendors_100_percent']}")
        print(f"  90%+ Success:         {self.overall_stats['vendors_90_percent_plus']}")
        print(f"  With Failures:        {self.overall_stats['vendors_with_failures']}")

        # Top vendors by MIB count
        print(f"\n{'=' * 80}")
        print("Top 20 Vendors by MIB Count")
        print(f"{'=' * 80}")
        sorted_vendors = sorted(
            self.vendor_results.values(),
            key=lambda x: x['total'],
            reverse=True
        )[:20]

        print(f"{'Vendor':<30} {'Total':<8} {'Passed':<8} {'Failed':<8} {'Rate':<8}")
        print("-" * 80)
        for result in sorted_vendors:
            print(f"{result['vendor']:<30} {result['total']:<8} "
                  f"{result['passed']:<8} {result['failed']:<8} "
                  f"{result['success_rate']:.1f}%")

        # Vendors with highest failure rates
        vendors_with_failures = [
            v for v in self.vendor_results.values()
            if v['failed'] > 0 and v['total'] >= 5
        ]

        if vendors_with_failures:
            print(f"\n{'=' * 80}")
            print("Vendors with Lowest Success Rates (min 5 MIBs)")
            print(f"{'=' * 80}")
            sorted_failures = sorted(
                vendors_with_failures,
                key=lambda x: x['success_rate']
            )[:20]

            print(f"{'Vendor':<30} {'Total':<8} {'Passed':<8} {'Failed':<8} {'Rate':<8}")
            print("-" * 80)
            for result in sorted_failures:
                print(f"{result['vendor']:<30} {result['total']:<8} "
                      f"{result['passed']:<8} {result['failed']:<8} "
                      f"{result['success_rate']:.1f}%")

        # Perfect vendors
        perfect_vendors = [
            v for v in self.vendor_results.values()
            if v['success_rate'] == 100.0 and v['total'] > 0
        ]

        if perfect_vendors:
            print(f"\n{'=' * 80}")
            print(f"Vendors with 100% Success Rate ({len(perfect_vendors)} total)")
            print(f"{'=' * 80}")
            print(", ".join(sorted([v['vendor'] for v in perfect_vendors])))

    def generate_markdown_report(self, output_file: Path):
        """Generate a markdown report suitable for README."""
        with open(output_file, 'w') as f:
            f.write("# MIB Validation Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Overall stats
            f.write("## Overall Statistics\n\n")
            f.write(f"- **Total Vendors:** {self.overall_stats['total_vendors']}\n")
            f.write(f"- **Total MIBs:** {self.overall_stats['total_mibs']}\n")
            f.write(f"- **Successfully Validated:** {self.overall_stats['total_passed']}\n")
            f.write(f"- **Failed Validation:** {self.overall_stats['total_failed']}\n")

            overall_success = 0
            if self.overall_stats['total_mibs'] > 0:
                overall_success = (self.overall_stats['total_passed'] /
                                   self.overall_stats['total_mibs'] * 100)
            f.write(f"- **Overall Success Rate:** {overall_success:.2f}%\n\n")

            # Vendor categories
            f.write("## Vendor Quality Distribution\n\n")
            f.write(f"- **100% Success:** {self.overall_stats['vendors_100_percent']} vendors\n")
            f.write(f"- **90%+ Success:** {self.overall_stats['vendors_90_percent_plus']} vendors\n")
            f.write(f"- **With Some Failures:** {self.overall_stats['vendors_with_failures']} vendors\n\n")

            # Top vendors
            f.write("## Major Vendors (by MIB count)\n\n")
            sorted_vendors = sorted(
                self.vendor_results.values(),
                key=lambda x: x['total'],
                reverse=True
            )[:30]

            f.write("| Vendor | Total MIBs | Passed | Failed | Success Rate |\n")
            f.write("|--------|------------|--------|--------|-------------|\n")
            for result in sorted_vendors:
                f.write(f"| {result['vendor']} | {result['total']} | "
                        f"{result['passed']} | {result['failed']} | "
                        f"{result['success_rate']:.1f}% |\n")

            f.write("\n## Notes\n\n")
            f.write("- MIBs are compiled from LibreNMS repository\n")
            f.write("- Validation tests if MIBs can be loaded by PySNMP\n")
            f.write("- Some failures are due to vendor-specific extensions or dependencies\n")
            f.write("- High failure rates may indicate legacy/obsolete equipment\n")

        print(f"\nMarkdown report saved: {output_file}")

    def save_json_report(self, output_file: Path):
        """Save detailed JSON report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'input_directory': str(self.input_dir),
            'overall_stats': self.overall_stats,
            'vendor_results': self.vendor_results
        }

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"JSON report saved: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Batch validate compiled MIBs across all vendors',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate all vendors
  %(prog)s --input ./compiled_mibs

  # Generate reports
  %(prog)s --input ./compiled_mibs --output validation_report.json --markdown VALIDATION.md

  # Verbose output
  %(prog)s --input ./compiled_mibs -v
        """
    )

    parser.add_argument('--input', '-i', type=str, required=True,
                        help='Directory containing vendor MIB subdirectories')
    parser.add_argument('--output', '-o', type=str,
                        help='Output JSON report file (default: validation_report.json)')
    parser.add_argument('--markdown', '-m', type=str,
                        help='Output markdown report file')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    input_dir = Path(args.input)
    if not input_dir.exists():
        print(f"ERROR: Input directory does not exist: {input_dir}")
        sys.exit(1)

    validator = BatchMibValidator(input_dir, args.verbose)

    try:
        start_time = datetime.now()
        validator.validate_all()
        duration = (datetime.now() - start_time).total_seconds()

        validator.print_summary()

        print(f"\nValidation completed in {duration:.1f} seconds ({duration / 60:.1f} minutes)")

        # Save reports
        output_file = Path(args.output) if args.output else input_dir / 'validation_report.json'
        validator.save_json_report(output_file)

        if args.markdown:
            validator.generate_markdown_report(Path(args.markdown))

        # Exit with error if overall success rate is below 80%
        overall_success = (validator.overall_stats['total_passed'] /
                           validator.overall_stats['total_mibs'] * 100)
        if overall_success < 80:
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