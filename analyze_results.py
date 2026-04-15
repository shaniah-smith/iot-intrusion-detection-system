import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("results/detection_results.csv")

# -------- Graph 1 (you already have) --------
label_counts = df["label"].value_counts()

plt.figure()
label_counts.plot(kind="bar")
plt.title("Detection Results Count")
plt.xlabel("Label")
plt.ylabel("Count")
plt.savefig("results/label_counts.png")
plt.close()

# -------- Graph 2 (Packet count per window) --------
plt.figure()
plt.plot(df["packet_count"])
plt.title("Packet Count per Window")
plt.xlabel("Window")
plt.ylabel("Packet Count")
plt.savefig("results/packet_count_per_window.png")
plt.close()

# -------- Graph 3 (Avg packet size) --------
plt.figure()
plt.plot(df["avg_packet_size"])
plt.title("Average Packet Size per Window")
plt.xlabel("Window")
plt.ylabel("Avg Packet Size")
plt.savefig("results/avg_packet_size_per_window.png")
plt.close()

print(" Graphs saved in results/ folder")
