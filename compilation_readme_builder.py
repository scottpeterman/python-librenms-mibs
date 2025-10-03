#!/usr/bin/env python3
# compilation_readme_builder.py
"""
Build a README-friendly Markdown table from your compilation JSON.

✅ Works with the JSON shape you posted (top-level "vendors" is a dict whose
   values contain "stats": {"compiled","failed","total"} and "compile_time").

Usage:
  python compilation_readme_builder.py CONVERSION.json CONVERSION_REPORT.md
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def load_json(path_str):
    p = Path(path_str)
    with p.open('r', encoding='utf-8') as f:
        return json.load(f)

def safe_int(v, default=0):
    try:
        return int(v)
    except Exception:
        return default

def safe_float(v, default=0.0):
    try:
        return float(v)
    except Exception:
        return default

def normalize_rows_from_vendors_dict(vendors_obj):
    """
    Input: dict like {"cisco": {"vendor": "cisco", "compile_time": 12.3, "stats": {...}}, ...}
    Output: list of row dicts with keys: vendor, compiled, failed, total, time_s, success_rate
    """
    rows = []

    # iterate stable-sorted by vendor key
    vendor_names = list(vendors_obj.keys())
    vendor_names.sort()

    i = 0
    while i < len(vendor_names):
        key = vendor_names[i]
        payload = vendors_obj.get(key)

        vendor_name = key
        if isinstance(payload, dict):
            if 'vendor' in payload and isinstance(payload['vendor'], str) and len(payload['vendor']) > 0:
                vendor_name = payload['vendor']

        compiled = 0
        failed = 0
        total = 0
        time_s = 0.0

        if isinstance(payload, dict):
            # stats
            stats = payload.get('stats')
            if isinstance(stats, dict):
                compiled = safe_int(stats.get('compiled'), 0)
                failed = safe_int(stats.get('failed'), 0)
                total = safe_int(stats.get('total'), compiled + failed)
            # time
            time_s = safe_float(payload.get('compile_time'), 0.0)

        denom = float(compiled + failed)
        success_rate = 0.0
        if denom > 0.0:
            success_rate = (compiled / denom) * 100.0

        row = {
            'vendor': vendor_name,
            'compiled': compiled,
            'failed': failed,
            'total': total,
            'time_s': time_s,
            'success_rate': success_rate
        }
        rows.append(row)
        i = i + 1

    return rows

def write_markdown(rows, top, out_path):
    """
    rows: list of dicts as built above
    top:  the full parsed JSON (to read total_time etc.)
    """
    # compute totals
    total_vendors = 0
    total_compiled = 0
    total_failed = 0
    i = 0
    while i < len(rows):
        total_vendors = total_vendors + 1
        total_compiled = total_compiled + safe_int(rows[i]['compiled'], 0)
        total_failed = total_failed + safe_int(rows[i]['failed'], 0)
        i = i + 1

    overall_rate = 0.0
    denom = float(total_compiled + total_failed)
    if denom > 0.0:
        overall_rate = (total_compiled / denom) * 100.0

    total_time = safe_float(top.get('total_time'), 0.0)

    with Path(out_path).open('w', encoding='utf-8') as f:
        f.write("# MIB Compilation Coverage\n\n")
        f.write("**Source:** LibreNMS MIBs • **Compiler:** PySMI → PySNMP • **Report:** auto-generated\n\n")
        ts = top.get('timestamp')
        if not isinstance(ts, str) or len(ts) == 0:
            ts = datetime.utcnow().isoformat() + "Z"
        f.write(f"_Generated: {ts}_\n\n")

        f.write("## Summary\n\n")
        f.write(f"- Vendors processed: **{total_vendors}**\n")
        f.write(f"- Compiled modules: **{total_compiled}**\n")
        f.write(f"- Failed modules: **{total_failed}**\n")
        f.write(f"- Overall success rate: **{overall_rate:.1f}%**\n")
        f.write(f"- Total compile time: **{total_time:.1f} s** ({total_time/60.0:.1f} minutes)\n\n")

        f.write("## Vendors (sorted by compiled count)\n\n")
        f.write("| Vendor | Compiled | Failed | Success | Time (s) |\n")
        f.write("|---|---:|---:|---:|---:|\n")

        # sort rows by compiled desc
        rows.sort(key=lambda r: (r.get('compiled') or 0), reverse=True)

        j = 0
        while j < len(rows):
            r = rows[j]
            name = r.get('vendor') or ''
            comp = safe_int(r.get('compiled'), 0)
            fail = safe_int(r.get('failed'), 0)
            rate = 0.0
            denom = float(comp + fail)
            if denom > 0.0:
                rate = (comp / denom) * 100.0
            secs = safe_float(r.get('time_s'), 0.0)
            f.write(f"| {name} | {comp} | {fail} | {rate:.1f}% | {secs:.1f} |\n")
            j = j + 1

def main():
    if len(sys.argv) < 3:
        print("Usage: compilation_readme_builder.py INPUT.json OUT.md")
        sys.exit(2)

    data = load_json(sys.argv[1])

    # Expect your posted schema
    vendors_obj = data.get('vendors')
    if not isinstance(vendors_obj, dict):
        print("ERROR: JSON does not have a top-level 'vendors' object (dict).")
        print("       Please pass your CONVERSION.json from the compiler run.")
        sys.exit(1)

    rows = normalize_rows_from_vendors_dict(vendors_obj)
    write_markdown(rows, data, sys.argv[2])
    print(f"Wrote: {sys.argv[2]}")

if __name__ == "__main__":
    main()
