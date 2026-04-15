import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("results/detection_results.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nLabel counts:")
print(df["label"].value_counts())

# Graph 1: NORMAL vs ALERT count
label_counts = df["label"].value_counts()
plt.figure(figsize=(8, 5))
label_counts.plot(kind="bar")
plt.title("Detection Results Count")
plt.xlabel("Label")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("results/label_counts.png")
plt.show()

# Graph 2: Packet count per window
plt.figure(figsize=(10, 5))
plt.plot(df["packet_count"].values, marker="o")
plt.title("Packet Count per Detection Window")
plt.xlabel("Window Index")
plt.ylabel("Packet Count")
plt.tight_layout()
plt.savefig("results/packet_count_per_window.png")
plt.show()

# Graph 3: Average packet size per window
plt.figure(figsize=(10, 5))
plt.plot(df["avg_packet_size"].values, marker="o")
plt.title("Average Packet Size per Detection Window")
plt.xlabel("Window Index")
plt.ylabel("Average Packet Size")
plt.tight_layout()
plt.savefig("results/avg_packet_size_per_window.png")
plt.show()