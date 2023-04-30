size = int(input())

matrix = []
alice_pos = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[alice_pos[0]][alice_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    r = alice_pos[0] + directions[direction][0]
    c = alice_pos[1] + directions[direction][1]

    if not (0 <= r < size and 0 <= c < size):
        print("Alice didn't make it to the tea party.")
        break
    elif matrix[r][c] == "R":
        matrix[r][c] = "*"
        print("Alice didn't make it to the tea party.")
        break
    elif matrix[r][c].isdigit():
        tea_bags += int(matrix[r][c])
    matrix[r][c] = "*"
    alice_pos = [r, c]

else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row)