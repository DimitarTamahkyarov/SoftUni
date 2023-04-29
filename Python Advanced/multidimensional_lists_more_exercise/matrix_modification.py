n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    r = int(command[1])
    c = int(command[2])
    v = int(command[3])

    if not (0 <= r < n and 0 <= c < n):
        print("Invalid coordinates")
        continue

    if command[0] == "Add":
        matrix[r][c] += v
    elif command[0] == "Subtract":
        matrix[r][c] -= v

for row in matrix:
    print(*row)
