import os

folder = "MyFiles"

# Create a folder automatically
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created successfully!")
else:
    print("Folder already exists.")

# Create a text file
file_path = os.path.join(folder, "report.txt")

with open(file_path, "w") as file:
    file.write("This file was created automatically using Python.")

print("Task completed successfully!")
