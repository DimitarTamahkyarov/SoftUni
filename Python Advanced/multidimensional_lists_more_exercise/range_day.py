matrix = []
position = []
targets = 0
hit_tagdets = []
killed = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            position = [row, col]
            matrix[row][col] = "."
        elif matrix[row][col] == "x":
            targets += 1

r = position[0]
c = position[1]

for _ in range(int(input())):
    info = input().split()
    command = info[0]
    direction = info[1]
    curr_pos_row = r
    curr_pos_col = c

    if command == "move":
        steps = int(info[2])
        curr_pos_row += directions[direction][0] * steps
        curr_pos_col += directions[direction][1] * steps
        if 0 <= curr_pos_row < 5 and 0 <= curr_pos_col < 5 and matrix[curr_pos_row][curr_pos_col] != "x":
            r = curr_pos_row
            c = curr_pos_col

    elif command == "shoot":
        while True:
            curr_pos_row += directions[direction][0]
            curr_pos_col += directions[direction][1]

            if not (0 <= curr_pos_row < 5 and 0 <= curr_pos_col < 5):
                break

            if matrix[curr_pos_row][curr_pos_col] == "x":
                matrix[curr_pos_row][curr_pos_col] = "."
                killed += 1
                hit_tagdets.append([curr_pos_row, curr_pos_col])
                break

    if killed == targets:
        break

if killed == targets:
    print(f"Training completed! All {killed} targets hit.")
else:
    print(f"Training not completed! {targets - killed} targets left.")

print(*hit_tagdets, sep="\n")