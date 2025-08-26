filename = input("Enter a file to read: ")

try:
    with open(filename, "r") as f:
        lines = [line.upper() for line in f]

    with open("output.txt", "w") as f:
        f.writelines(lines)

    print("Modified content to be wrriten 'output.txt'.")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except PermissionError:
    print(f"Error: Permission denied unable to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

