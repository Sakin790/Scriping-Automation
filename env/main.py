import os

# Get an environment variable
home = os.getenv("HOME")
print(home)  # Output: /home/username

# Set a new environment variable
os.environ["MY_APP"] = "test_app"
print(os.getenv("MY_APP"))  # Output: test_app