size = int(input())

matrix = [list(input()) for _ in range(size)]
knights = 0

positions = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2))

while True:
    is_finish = True
    knight_biggest_attacker = []
    most_attacks = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                curr_atacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            curr_atacks += 1
                            is_finish = False
                if curr_atacks > most_attacks:
                    most_attacks = curr_atacks
                    knight_biggest_attacker = [row, col]

    if knight_biggest_attacker:
        matrix[knight_biggest_attacker[0]][knight_biggest_attacker[1]] = "0"
        knights += 1
    if is_finish:
        print(knights)
        break







