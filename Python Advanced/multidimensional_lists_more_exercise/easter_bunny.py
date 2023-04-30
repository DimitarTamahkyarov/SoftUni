size = int(input())
matrix = [input().split() for _ in range(size)]

staring_position = []
path = []
total_sum = 0
direct = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            staring_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for way, direction in directions.items():
    curr_sum = 0
    curr_path = []
    r = staring_position[0] + direction[0]
    c = staring_position[1] + direction[1]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "X":
            break
        else:
            curr_sum += int(matrix[r][c])
            curr_path.append([r, c])
        r += direction[0]
        c += direction[1]

    if curr_sum > total_sum:
        direct = way
        total_sum = curr_sum
        path = curr_path

print(direct)
print(*path, sep="\n")
print(total_sum)