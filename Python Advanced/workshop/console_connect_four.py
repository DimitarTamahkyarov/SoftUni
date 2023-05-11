def create_field(row: int, col: int):
    while row < 4:
        print("The rows must be 4 or more!")
        row = int(input("Please, insert valid number for col! "))
        print()
    while col < 4:
        print("The cols must be 4 or more!")
        col = int(input("Please, insert valid number for col! "))
        print()

    matrix = [[0 for _ in range(col)] for _ in range(row)]

    return matrix


def player_action(player: int, num: int, matrix: list):
    player_choice = int(num)-1
    for i in range(len(matrix)-1, -1, -1):
        if matrix[i][player_choice] == 0:
            matrix[i][player_choice] = player
            return i, player_choice


def check_for_winner(matrix: list, r, c):
    winner = 0
    el = matrix[r][c]
    row_size = len(matrix)
    col_size = len(matrix[0])

    for direction in directions:
        for direct in directions[direction]:
            curr_r = r + direct[0]
            curr_c = c + direct[1]
            if 0 <= curr_r < row_size and 0 <= curr_c < col_size:
                if el == matrix[curr_r][curr_c]:
                    winner = el
                else:
                    winner = 0
                    break
            else:
                winner = 0
                break
        else:
            return winner

    return winner


def print_matrix(matrix):
    for line in matrix:
        print(line)

# >-------------------> Program Start From Here <-------------------<

directions = {
    "up": [(-1, 0), (-2, 0), (-3, 0)],
    "down": [(1, 0), (2, 0), (3, 0)],
    "left": [(0, -1), (0, -2), (0, -3)],
    "right": [(0, 1), (0, 2), (0, 3)],
    "down right diagonal": [(1, 1), (2, 2), (3, 3)],
    "up right diagonal": [(-1, 1), (-2, 2), (-3, 3)],
    "up left diagonal": [(-1, -1), (-2, -2), (-3, -3)],
    "down left diagonal": [(1, -1), (2, -2), (3, -3)]
}

rows = int(input("Please insert rows: "))
cols = int(input("Please insert cols: "))
field = create_field(rows, cols)
counter = 0
while True:
    counter += 1
    row = 0
    col = 0
    if counter % 2 == 1:
        row, col = player_action(1, int(input("Player 1, please choose c column: ")), field)
    else:
        row, col = player_action(2, int(input("Player 2, please choose c column: ")), field)

    print_matrix(field)

    result = check_for_winner(field, row, col)
    if result != 0:
        print(f"The Winner is {result}")
        break
