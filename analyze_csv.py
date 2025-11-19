import csv

file = "sample.csv"

rows = []

try:
    with open(file, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            rows.append(row)

    print("Columns:", header)
    print("Total Rows:", len(rows))
    print("First 5 Rows:")
    for r in rows[:5]:
        print(r)

except FileNotFoundError:
    print(f"Error: {file} not found. Make sure sample.csv is in the same folder!")
