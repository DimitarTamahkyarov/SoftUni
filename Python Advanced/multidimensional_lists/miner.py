n = int(input())
moves = [input().split()]
field = [input().split() for _ in range(n)]
position = []
coals = 0
total_coals = 0

for r in range(n):
    for c in range(n):
        if field[r][c] == "s":
            position.append(r)
            position.append(c)
        if field[r][c] == "c":
            total_coals += 1

for move in moves:
    if move == "up" and position[0] > 0:
        position[0] -= 1
    elif move == "down" and position[0] < n-1:
        position[0] += 1
    elif move == "left" and position[1] > 0:
        position[1] -= 1
    elif move == "right" and position[1] < n-1:
        position[1] += 1
    else:
        continue

    r = position[0]
    c = position[1]

    if field[r][c] == "c":
        coals += 1
        field[r][c] = "*"
    if coals == total_coals:
        print(f"You collected all coal! ({r}, {c})")
        break
    if field[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break
else:
    print(f"{total_coals-coals} pieces of coal left. ({position[0]}, {position[1]})")