def is_valid_command(command_type):
    result = True
    if len(command_type) != 5:
        result = False
    elif command_type[0] != "swap":
        result = False
    elif int(command_type[1]) >= rows or int(command_type[1]) < 0:
        result = False
    elif int(command_type[2]) >= cols or int(command_type[2]) < 0:
        result = False
    elif int(command_type[3]) >= rows or int(command_type[3]) < 0:
        result = False
    elif int(command_type[4]) >= cols or int(command_type[4]) < 0:
        result = False

    return result


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for r in range(rows)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    if is_valid_command(command):
        r1 = int(command[1])
        c1 = int(command[2])
        r2 = int(command[3])
        c2 = int(command[4])

        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

        for r in range(rows):
            print(*matrix[r])
    else:
        print("Invalid input!")