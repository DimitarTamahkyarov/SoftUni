
presents = int(input())
size = int(input())
neighborhood = []
santa_pos = []
nice_kids = 0
nice_kids_get_present = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    neighborhood.append(input().split())
    for col in range(size):
        if neighborhood[row][col] == "S":
            santa_pos = [row, col]
            neighborhood[row][col] = "-"
        elif neighborhood[row][col] == "V":
            nice_kids += 1

while santa_pos:
    command = input()

    if command == "Christmas morning" or presents == 0:
        if nice_kids > nice_kids_get_present and presents == 0:
            print("Santa ran out of presents!")
        break

    r = santa_pos[0] + directions[command][0]
    c = santa_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        continue

    if neighborhood[r][c] == "V":
        neighborhood[r][c] = "-"
        presents -= 1
        nice_kids_get_present += 1

    elif neighborhood[r][c] == "X":
        neighborhood[r][c] = "-"

    elif neighborhood[r][c] == "C":
        for direction in directions.values():
            if neighborhood[r + direction[0]][c + direction[1]] == "V":
                presents -= 1
                nice_kids_get_present += 1
            elif neighborhood[r + direction[0]][c + direction[1]] == "X":
                presents -= 1
            neighborhood[r + direction[0]][c + direction[1]] = "-"

            if presents == 0:
                break

    santa_pos = [r, c]
if santa_pos:
    neighborhood[santa_pos[0]][santa_pos[1]] = "S"

for row in neighborhood:
    print(*row)

if nice_kids == nice_kids_get_present:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_get_present} nice kid/s.")