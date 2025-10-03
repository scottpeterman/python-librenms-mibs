#!/usr/bin/env python3
"""
Generate interactive HTML validation report with charts.
Uses Chart.js for better-looking visualizations.

Usage:
    python generate_validation_report.py validation_report.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def generate_html_report(json_file: str, output_file: str = "validation_report.html"):
    """Generate interactive HTML report from validation JSON."""

    with open(json_file, 'r') as f:
        data = json.load(f)

    overall = data['overall_stats']
    vendors = data['vendor_results']

    # Sort vendors by total MIBs
    vendor_list = sorted(vendors.items(), key=lambda x: x[1]['total'], reverse=True)

    # Top 30 vendors for main chart
    top_vendors = vendor_list[:30]
    top_labels = [v[0] for v in top_vendors]
    top_totals = [v[1]['total'] for v in top_vendors]
    top_rates = [v[1]['success_rate'] for v in top_vendors]

    # Firewall vendors
    fw_vendors = ['fortinet', 'watchguard', 'paloaltonetworks', 'sonicwall', 'checkpoint']
    fw_data = [(v, vendors[v]) for v in fw_vendors if v in vendors]
    fw_labels = [v[0] for v in fw_data]
    fw_totals = [v[1]['total'] for v in fw_data]
    fw_rates = [v[1]['success_rate'] for v in fw_data]

    # Load balancer vendors
    lb_vendors = ['f5', 'radware', 'citrix', 'kemp', 'arraynetworks']
    lb_data = [(v, vendors[v]) for v in lb_vendors if v in vendors]
    lb_labels = [v[0] for v in lb_data]
    lb_totals = [v[1]['total'] for v in lb_data]
    lb_rates = [v[1]['success_rate'] for v in lb_data]

    # Build vendor table (top 50)
    vendor_table_rows = []
    for vendor_name, vendor_data in vendor_list[:50]:
        vendor_table_rows.append(f"""
<tr>
<td>{vendor_name}</td>
<td>{vendor_data['total']}</td>
<td>{vendor_data['passed']}</td>
<td>{vendor_data['failed']}</td>
<td>{vendor_data['success_rate']:.1f}%</td>
</tr>""")

    # Firewall table
    fw_table_rows = []
    for vendor_name, vendor_data in fw_data:
        fw_table_rows.append(f"""
<tr>
<td>{vendor_name}</td>
<td>{vendor_data['total']}</td>
<td>{vendor_data['passed']}</td>
<td>{vendor_data['failed']}</td>
<td>{vendor_data['success_rate']:.1f}%</td>
</tr>""")

    # Load balancer table
    lb_table_rows = []
    for vendor_name, vendor_data in lb_data:
        lb_table_rows.append(f"""
<tr>
<td>{vendor_name}</td>
<td>{vendor_data['total']}</td>
<td>{vendor_data['passed']}</td>
<td>{vendor_data['failed']}</td>
<td>{vendor_data['success_rate']:.1f}%</td>
</tr>""")

    html_content = f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'/>
<meta name='viewport' content='width=device-width, initial-scale=1'/>
<title>Validation Report</title>
<link rel='preconnect' href='https://cdn.jsdelivr.net'/>
<script src='https://cdn.jsdelivr.net/npm/chart.js'></script>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif; margin:24px; background:#fafafa;}}
h1{{margin:0 0 8px 0; color:#1a1a1a;}} 
h2{{margin-top:28px; color:#2a2a2a;}} 
h3{{margin-top:22px; color:#3a3a3a;}}
.meta{{color:#666;margin-bottom:16px; font-size:14px;}}
table{{border-collapse:collapse;width:100%;margin-top:12px; background:white; box-shadow:0 1px 3px rgba(0,0,0,0.1);}}
th,td{{border:1px solid #e0e0e0;padding:10px;vertical-align:top;}}
th{{background:#f5f5f5;text-align:left; font-weight:600;}}
tbody tr:nth-child(even){{background:#fafafa;}}
tbody tr:hover{{background:#f0f7ff;}}
.grid{{display:grid;grid-template-columns:1fr;gap:24px;}}
@media(min-width:1000px){{.grid{{grid-template-columns:1fr 1fr;}}}}
.card{{padding:20px;border:1px solid #e0e0e0;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.05); background:white;}}
.chart-container{{position:relative; height:400px; width:100%;}}
canvas{{width:100%!important; height:100%!important;}}
.pill{{display:inline-block;border:1px solid #ddd;border-radius:20px;padding:4px 14px;margin:4px 8px 4px 0;font-size:13px;color:#333;background:#fff; box-shadow:0 1px 2px rgba(0,0,0,0.05);}}
.stat-badge{{background:linear-gradient(135deg, #667eea 0%, #764ba2 100%); color:white;}}
.header-section{{background:white; padding:24px; border-radius:8px; margin-bottom:24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);}}
</style>
</head>
<body>
<div class='header-section'>
<h1>SNMP MIB Validation Report</h1>
<div class='meta'>Generated: {data['timestamp']}</div>
<div>
<span class='pill stat-badge'>Total vendors: {overall['total_vendors']}</span> 
<span class='pill stat-badge'>Total MIBs: {overall['total_mibs']}</span> 
<span class='pill'>Passed: {overall['total_passed']}</span> 
<span class='pill'>Failed: {overall['total_failed']}</span> 
<span class='pill'>100% vendors: {overall['vendors_100_percent']}</span> 
<span class='pill'>90%+ vendors: {overall['vendors_90_percent_plus']}</span> 
<span class='pill'>With failures: {overall['vendors_with_failures']}</span>
</div>
</div>

<div class='grid' style='margin-top:24px;'>
<div class='card'><h2>Top Vendors by MIB Coverage</h2><div class='chart-container'><canvas id='chartTop'></canvas></div></div>
<div class='card'><h2>Firewalls</h2><div class='chart-container'><canvas id='chartFW'></canvas></div></div>
<div class='card'><h2>Load Balancers / ADC</h2><div class='chart-container'><canvas id='chartLB'></canvas></div></div>
</div>

<div class='grid' style='margin-top:24px;'>
<div class='card'>
<h2>Major Vendors (by total MIBs)</h2>
<table>
<thead><tr><th>Vendor</th><th>Total</th><th>Passed</th><th>Failed</th><th>Success</th></tr></thead>
<tbody>
{''.join(vendor_table_rows)}
</tbody></table></div>

<div class='card'>
<h2>Firewalls</h2>
<table>
<thead><tr><th>Vendor</th><th>Total</th><th>Passed</th><th>Failed</th><th>Success</th></tr></thead>
<tbody>
{''.join(fw_table_rows)}
</tbody></table>

<h2 style='margin-top:32px;'>Load Balancers / ADC</h2>
<table>
<thead><tr><th>Vendor</th><th>Total</th><th>Passed</th><th>Failed</th><th>Success</th></tr></thead>
<tbody>
{''.join(lb_table_rows)}
</tbody></table>
</div>
</div>

<script>
const labelsTop = {json.dumps(top_labels)};
const totalsTop = {json.dumps(top_totals)};
const ratesTop  = {json.dumps(top_rates)};
const fwLabels  = {json.dumps(fw_labels)};
const fwTotals  = {json.dumps(fw_totals)};
const fwRates   = {json.dumps(fw_rates)};
const lbLabels  = {json.dumps(lb_labels)};
const lbTotals  = {json.dumps(lb_totals)};
const lbRates   = {json.dumps(lb_rates)};

function makeBarLineChart(canvasId, labels, barData, lineData, title){{
  const ctx = document.getElementById(canvasId).getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels: labels,
      datasets: [
        {{ 
          label: 'Total MIBs', 
          data: barData, 
          backgroundColor: 'rgba(102, 126, 234, 0.7)',
          borderColor: 'rgba(102, 126, 234, 1)',
          borderWidth: 2,
          yAxisID: 'y',
          order: 2
        }},
        {{ 
          label: 'Success %', 
          data: lineData, 
          type: 'line',
          borderColor: 'rgba(16, 185, 129, 1)',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          borderWidth: 3,
          pointRadius: 5,
          pointHoverRadius: 7,
          pointBackgroundColor: 'rgba(16, 185, 129, 1)',
          pointBorderColor: '#fff',
          pointBorderWidth: 2,
          yAxisID: 'y1',
          tension: 0.4,
          fill: false,
          order: 1
        }}
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: true,
      aspectRatio: 2,
      plugins: {{
        title: {{ 
          display: true, 
          text: title, 
          font: {{ size: 16, weight: 'bold' }},
          padding: {{ top: 10, bottom: 20 }}
        }},
        legend: {{ 
          position: 'top',
          labels: {{
            padding: 15,
            font: {{ size: 12 }}
          }}
        }},
        tooltip: {{ 
          mode: 'index', 
          intersect: false,
          backgroundColor: 'rgba(0, 0, 0, 0.8)',
          padding: 12,
          titleFont: {{ size: 13, weight: 'bold' }},
          bodyFont: {{ size: 12 }},
          callbacks: {{
            label: function(context) {{
              let label = context.dataset.label || '';
              if (label) {{
                label += ': ';
              }}
              if (context.parsed.y !== null) {{
                if (context.datasetIndex === 1) {{
                  label += context.parsed.y.toFixed(1) + '%';
                }} else {{
                  label += context.parsed.y;
                }}
              }}
              return label;
            }}
          }}
        }}
      }},
      interaction: {{ mode: 'index', intersect: false }},
      scales: {{
        y: {{ 
          beginAtZero: true,
          position: 'left',
          title: {{ display: true, text: 'Total MIBs', font: {{ weight: 'bold', size: 12 }} }},
          grid: {{ color: 'rgba(0, 0, 0, 0.08)' }},
          ticks: {{
            padding: 8
          }}
        }},
        y1: {{ 
          beginAtZero: true, 
          position: 'right', 
          min: 0, 
          max: 100,
          title: {{ display: true, text: 'Success %', font: {{ weight: 'bold', size: 12 }} }}, 
          grid: {{ drawOnChartArea: false }},
          ticks: {{
            callback: function(value) {{
              return value + '%';
            }},
            padding: 8
          }}
        }},
        x: {{ 
          ticks: {{ 
            autoSkip: false, 
            maxRotation: 45, 
            minRotation: 45,
            font: {{ size: 10 }}
          }},
          grid: {{ display: false }}
        }}
      }}
    }}
  }});
}}

makeBarLineChart('chartTop', labelsTop, totalsTop, ratesTop, 'Top Vendors by Total & Success %');
makeBarLineChart('chartFW',  fwLabels,  fwTotals,  fwRates,  'Firewalls: Total & Success %');
makeBarLineChart('chartLB',  lbLabels,  lbTotals,  lbRates,  'Load Balancers / ADC: Total & Success %');

</script>
</body></html>"""

    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"Generated: {output_file}")
    print(f"Vendors: {overall['total_vendors']}")
    print(f"MIBs: {overall['total_mibs']}")
    print(f"Success: {overall['total_passed'] / overall['total_mibs'] * 100:.2f}%")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_validation_report.py validation_report.json")
        sys.exit(1)

    json_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "validation_report.html"

    generate_html_report(json_file, output_file)