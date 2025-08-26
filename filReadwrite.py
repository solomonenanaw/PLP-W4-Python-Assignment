
import os

if not os.path.exists("input.txt"):
    with open("input.txt", "w") as f:
        f.write("Hello world\nThis is a test.")

with open("input.txt", "r") as f:
    lines = [line.upper() for line in f]

with open("output.txt", "w") as f:
    f.writelines(lines)

print("Modified content written to 'output.txt'.")
