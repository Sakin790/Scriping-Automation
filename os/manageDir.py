import os

# Create a directory structure
os.makedirs("project/src", exist_ok=True)

# Create a file
with open("project/src/sample.txt", "w") as f:
    f.write("Hello, World!")

# List directory contents
print(os.listdir("project/src"))  # Output: ['sample.txt']

# Rename the file
os.rename("project/src/sample.txt", "project/src/example.txt")

# Delete the file
os.remove("project/src/example.txt")