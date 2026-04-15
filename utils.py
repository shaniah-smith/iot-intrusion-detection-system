import csv
import os


def save_result_to_csv(filename, row, header=None):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header or row.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)