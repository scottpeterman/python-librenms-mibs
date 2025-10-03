import json
import matplotlib.pyplot as plt

# Load the JSON report
with open("validation_report.json", "r") as f:
    data = json.load(f)

# Vendors of interest
selected_vendors = [
    "cisco", "junos", "comware", "nokia", "junose", "enterasys",
    "linksys", "transition", "ciena", "dlink", "dasan", "adva",
    "dell", "extreme", "hp", "screenos", "fortinet", "arubaos",
    "arubaos-cx", "a10", "f5", "paloaltonetworks"
]

# Extract counts
vendor_counts = {}
for entry in data["vendors"]:
    vendor = entry["Vendor"].lower()
    if vendor in selected_vendors:
        vendor_counts[vendor] = entry["Total MIBs"]

# Build lists for plotting
labels = list(vendor_counts.keys())
sizes = list(vendor_counts.values())

# Make pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct=lambda p: f'{int(p*sum(sizes)/100)}',
    startangle=120,        # rotate starting point to spread crowded labels
    labeldistance=1.05,    # move labels outward
    pctdistance=0.7        # move numbers inward
)

# Improve text size
for t in texts:
    t.set_fontsize(9)
for t in autotexts:
    t.set_fontsize(8)

ax.set_title("Selected Vendor Share by Total MIBs (Counts)")
plt.tight_layout()
plt.show()
