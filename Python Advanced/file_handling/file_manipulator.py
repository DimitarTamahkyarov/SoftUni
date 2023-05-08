import os

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    new_file = command[1]

    if command[0] == "Create":
        with open(f"files/{new_file}", "w") as file:
            pass
    elif command[0] == "Add":
        text = command[2]
        with open(f"files/{new_file}", "a") as file:
            file.write(text + "\n")
    elif command[0] == "Replace":
        old_text = command[2]
        new_text = command[3]
        try:
            with open(f"files/{new_file}") as file:
                text = file.read().replace(old_text, new_text)
            with open(f"files/{new_file}", "w") as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            os.remove(f"files/{new_file}")
        except FileNotFoundError:
            print("An error occurred")
