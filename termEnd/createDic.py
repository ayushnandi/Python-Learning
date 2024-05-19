import os

# Define the directory where you want to create the files
directory = "New Folder"

# List of filenames to be created
filenames = ["file1.txt", "file2.txt", "file3.txt"]

# Create the directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create and write to each file in the list
for filename in filenames:
    # Define the full path to the file
    filepath = os.path.join(directory, filename)
    
    # Open the file in write mode and write some text
    with open(filepath, "w") as file:
        file.write(f"This is the content of {filename}")
    
    print(f"Created {filepath}")

print("All files created successfully!")
