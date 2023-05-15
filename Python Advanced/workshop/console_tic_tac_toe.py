def take_and_check_the_number(num: int, matrix: list):
    is_not_free_position = True

    while is_not_free_position:
        while num < 1 or num > 9:
            print("Invalid position! Choose correct one! It should be between 1 and 9 both inclusive.")
            num = int(input("Choose free position: "))

        counter = 1

        for row in range(3):
            for col in range(3):
                if matrix[row][col] == num:
                    is_not_free_position = False
                    break
                counter += 1
        if counter == 9:
            print("This is not a free position!")
            num = int(input("Choose a free position: "))

    return num


def player_action(number, mark, matrix):
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == number:
                matrix[row][col] = mark


def print_matrix(matrix):
    result = []
    for row in range(3):
        for col in range(3):
            if matrix[row][col] not in ["X", "O"]:
                result.append(" ")
            else:
                result.append(matrix[row][col])

    print(f"| {result[0]} | {result[1]} | {result[2]} |")
    print(f"| {result[3]} | {result[4]} | {result[5]} |")
    print(f"| {result[6]} | {result[7]} | {result[8]} |")


# Start block

current_player = input("Player one name: ")
other_player = input("Player two name: ")
current_player_choice = input(f"{current_player} would you like to play with 'X' or 'O' ? ")
other_player_choice = "O" if current_player_choice == "X" else "X"

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print(f"{current_player} start first!")

# Play block

while True:
    print(f"{current_player} choose a free position [1-9]:", end=" ")
    player_choice = take_and_check_the_number(int(input()), board)
    player_mark = current_player_choice

    player_action(player_choice, player_mark, board)

    print_matrix(board)

    current_player, other_player = other_player, current_player
    current_player_choice, other_player_choice = other_player_choice, current_player_choice


