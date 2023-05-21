from collections import deque

size = int(input())
car_number = input()
car_position = [0, 0]
kilometers = 0
tunnel_coordinates = deque([])

matrix = [input().split() for row in range(size)]

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "T":
            tunnel_coordinates.append((row, col))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    row = 0
    col = 0

    try:
        row = car_position[0] + directions[command][0]
        col = car_position[1] + directions[command][1]

        if matrix[row][col] == ".":
            kilometers += 10
        elif matrix[row][col] == "T":
            if tunnel_coordinates[0] != (row, col):
                tunnel_coordinates.append(tunnel_coordinates.popleft())

            matrix[row][col] = "."
            row, col = tunnel_coordinates[1][0], tunnel_coordinates[1][1]
            matrix[row][col] = "."
            kilometers += 30
        elif matrix[row][col] == "F":
            print(f"Racing car {car_number} finished the stage!")
            kilometers += 10
            car_position = [row, col]
            break

    except IndexError:
        rol, col = 0, 0

    car_position = [row, col]

matrix[car_position[0]][car_position[1]] = "C"

print(f"Distance covered {kilometers} km.")

for row in matrix:
    print("".join(row))


