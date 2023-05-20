size = int(input())

battle_field = [[char for char in input()] for row in range(size)]
submarine_pos = []
submarine_damage = 0
hit_ships = 0

for row in range(size):
    for col in range(size):

        if battle_field[row][col] == "S":
            submarine_pos = [row, col]
            battle_field[row][col] = "-"
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    row = submarine_pos[0] + directions[command][0]
    col = submarine_pos[1] + directions[command][1]
    try:
        if battle_field[row][col] == "*":
            submarine_damage += 1
        elif battle_field[row][col] == "C":
            hit_ships += 1
        battle_field[row][col] = "-"
    except IndexError:
        continue

    if submarine_damage == 3:
        battle_field[row][col] = "S"
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break

    if hit_ships == 3:
        battle_field[row][col] = "S"
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    submarine_pos[0] = row
    submarine_pos[1] = col

for row in battle_field:
    print("".join(row))
