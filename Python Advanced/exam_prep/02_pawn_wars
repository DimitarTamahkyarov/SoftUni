def position(position: list) -> str:
    row = position[0]
    col = position[1]
    board_cols = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    board_rows = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}

    return f"{board_cols[col]}{board_rows[row]}"


board = [input().split() for row in range(8)]

white_pawn = []
black_pawn = []

for row in range(8):
    for col in range(8):
        if board[row][col] == 'w':
            white_pawn = [row, col]
        elif board[row][col] == 'b':
            black_pawn = [row, col]

while True:
    w_row = white_pawn[0]
    if w_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {position(white_pawn)}.")
        break
    w_col = white_pawn[1]
    try:
        if board[w_row - 1][w_col - 1] == "b":
            print(f"Game over! White win, capture on {position(black_pawn)}.")
            break
    except IndexError:
        pass

    try:
        if board[w_row - 1][w_col + 1] == "b":
            print(f"Game over! White win, capture on {position(black_pawn)}.")
            break
    except IndexError:
        pass

    board[white_pawn[0]][white_pawn[1]] = "-"
    white_pawn[0] -= 1
    board[white_pawn[0]][white_pawn[1]] = "w"

    if white_pawn[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {position(white_pawn)}.")
        break

    b_row = black_pawn[0]
    if b_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {position(black_pawn)}.")
        break
    b_col = black_pawn[1]

    if board[b_row + 1][b_col - 1] == "w" or board[b_row + 1][b_col + 1] == "w":
        print(f"Game over! Black win, capture on {position(white_pawn)}.")
        break

    board[black_pawn[0]][black_pawn[1]] = "-"
    black_pawn[0] += 1
    board[black_pawn[0]][black_pawn[1]] = "b"

    if black_pawn[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {position(black_pawn)}.")
        break



