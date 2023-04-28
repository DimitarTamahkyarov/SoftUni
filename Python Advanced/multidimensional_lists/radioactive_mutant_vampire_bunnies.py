n, m = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(n)]
commands = input()
r, c = -1, -1
is_win = False

for row in range(n):
    for col in range(m):
        if matrix[row][col] == "P":
            r, c = row, col

for command in commands:
    if r == -1 or c == -1:
        break
    matrix[r][c] = "."
    if command == "U" and r > 0:
        r -= 1
    elif command == "D" and r < n-1:
        r += 1
    elif command == "L" and c > 0:
        c -= 1
    elif command == "R" and c < m-1:
        c += 1
    else:
        is_win = True

    for row in range(n):
        for col in range(m):
            if matrix[row][col] == "B":
                if row > 0 and matrix[row-1][col] != "B":
                    matrix[row-1][col] = "b"
                if row < n - 1 and matrix[row+1][col] != "B":
                    matrix[row+1][col] = "b"
                if col > 0 and matrix[row][col-1] != "B":
                    matrix[row][col-1] = "b"
                if col < m - 1 and matrix[row][col+1] != "B":
                    matrix[row][col+1] = "b"

    for row in range(n):
        for col in range(m):
            if matrix[row][col] == "b":
                matrix[row][col] = "B"

    if is_win:
        break
    elif matrix[r][c] == "B":
        is_win = False
        break

for row in matrix:
    print(*row, sep="")

if is_win:
    print(f"won: {r} {c}")
else:
    print(f"dead: {r} {c}")
