import pandas as pd

files = {
    "normal_results.csv": "NORMAL",
    "dos_results.csv": "ALERT",
    "portscan_results.csv": "ALERT",
}

for filename, expected in files.items():
    path = f"results/{filename}"
    df = pd.read_csv(path)

    correct = (df["label"] == expected).sum()
    total = len(df)
    accuracy = correct / total if total > 0 else 0

    print(f"{filename}")
    print(f"Expected: {expected}")
    print(f"Correct: {correct}/{total}")
    print(f"Accuracy: {accuracy:.2%}")
    print("-" * 40)