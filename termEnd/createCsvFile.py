import csv

# Data to write to CSV file
data = [
    {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'},
    {'name': 'Jane Smith', 'age': 25, 'email': 'jane@example.com'},
    {'name': 'Emily Davis', 'age': 35, 'email': 'emily@example.com'}
]

# Specify the CSV file name
csv_file = 'people2.csv'

# Writing data to CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['name', 'age', 'email']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Reading data from CSV file into a dictionary
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    data_from_csv = [row for row in reader]

# Print the data read from the CSV file
for row in data_from_csv:
    print(row)
