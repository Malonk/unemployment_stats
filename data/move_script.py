import os

"""Script to move files from folders (a, b, c, ...) to folder x."""

old = "old"
base = os.path.abspath(os.path.join(os.path.dirname(__file__), old))

# Create list of directories to process
dirs = [x for x in os.listdir(base)
        if os.path.isdir(os.path.join(base, x))]

# Creat new dir if it doesn't alreay exist
new = os.path.join(base, "data")
if not os.path.exists(new):
    os.mkdir(new)

# Move files within folders
for folder in dirs:
    for filename in os.listdir(os.path.join(base, folder)):
        a = os.path.join(base, folder, filename)
        b = os.path.join(base, "data", filename)
        os.rename(a, b)
        print(f"Moved {a} to {b}")


