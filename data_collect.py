import json
import matplotlib.pyplot as plt
import numpy as np
from rich import print

json_file = input("Enter the json file name: ")

with open(f"data_collected/{json_file}.json") as f:
    data = json.load(f)

times = []
bandwidths = []

img = input("Enter the graph name that you want to save: ")

plt.style.use('fivethirtyeight')
plt.rcParams.update({"font.size": 12})

for i, interval in enumerate(data['intervals']):
    bps = interval['sum']['bits_per_second']
    times.append(i)
    bandwidths.append(bps / 1e6) # Mbps

window = 5
rolling_avg = np.convolve(bandwidths, np.ones(window)/window, mode="valid")

plt.figure(figsize=(14,6))

plt.plot(times, bandwidths, color="blue", linewidth=0.8, alpha=0.4, label="Download data limited to 5Mb")

plt.plot(times[:len(rolling_avg)], rolling_avg, color="red", linewidth=2, label=f"Rolling Average")

plt.title("iperf3 Throughput Test", fontsize=14, weight="bold")
plt.xlabel("Time (min)")
plt.ylabel("Throughput (Mbps)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save as PNG
plt.savefig(f"graphs/{img}.png", dpi=300, bbox_inches="tight")
print(f"Graph saved as {img}.png in the folder ~/launch_test/Graphs/")
