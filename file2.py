import os

# This works on ALL operating systems
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop, "roti.txt")

with open(file_path, "r") as file:
    print(file.read())