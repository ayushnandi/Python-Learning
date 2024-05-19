import csv

def write_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())

            # Write header
            writer.writeheader()

            # Write data
            writer.writerows(data)
        print(f"CSV file '{filename}' created and written successfully.")
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")

def read_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        print(f"CSV file '{filename}' read successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

# Test the functions
data = [
    {"Name": "John", "Age": 30, "City": "New York"},
    {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
    {"Name": "Bob", "Age": 35, "City": "Chicago"}
]
filename = "data.csv"
write_csv(filename, data)
data_read = read_csv(filename)
if data_read:
    print("Data read from CSV file:")
    for row in data_read:
        print(row)
