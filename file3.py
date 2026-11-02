from pathlib import Path

# Works on Windows, Mac, Linux
desktop = Path.home() / "Desktop" / "roti.txt"

with open(desktop, "r") as file:
    print(file.read())

# Or directly
content = Path.home().joinpath("Desktop", "roti.txt").read_text()
print(content)