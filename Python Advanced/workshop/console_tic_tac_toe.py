def take_and_check_the_number(num: int, matrix: list):
    while True:
        try:
            num = int(num)
        except ValueError:
            print("Invalid input!")
            num = input("Choose free position: ")
            continue
        while num < 1 or num > 9:
            print("Invalid position! Choose correct one! It should be between 1 and 9 both inclusive.")
            print()
            num = int(input("Choose free position: "))

        row = (num - 1) // 3
        col = (num - 1) % 3

        if matrix[row][col] == num:
            break
        else:
            print("This is not a free position!")
            print()
            num = int(input("Choose a free position: "))

    return num


def player_action(number, mark, matrix):
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == number:
                matrix[row][col] = mark


def win(matrix):
    pass


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


# Initialize the players

current_player = input("Player one name: ")
other_player = input("Player two name: ")
result = {current_player: 0, other_player: 0}

# Player choose the "X" or "O"

current_player_choice = input(f"{current_player} would you like to play with 'X' or 'O' ? ").upper()

while current_player_choice not in ["X", "O"]:
    print("Invalid input!")
    current_player_choice = input(f"{current_player} would you like to play with 'X' or 'O' ? ").upper()

other_player_choice = "O" if current_player_choice == "X" else "X"

while True:
    # Initialize the board

    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # Print info

    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{current_player} start first!")

    # Play block

    while True:
        print(f"{current_player} choose a free position [1-9]:", end=" ")
        player_choice = take_and_check_the_number(input(), board)
        player_mark = current_player_choice

        player_action(player_choice, player_mark, board)

        print_matrix(board)

        current_player, other_player = other_player, current_player
        current_player_choice, other_player_choice = other_player_choice, current_player_choice

        if win(board):
            break
    decision = input("Do you want another game? 'Y' or 'N'").upper()
    while decision not in ["Y", "N"]:
        print("I dont understand you. Try again!")
        decision = input("Do you want another game? 'Y' or 'N'").upper()

    if decision == "N":
        print(f"The Final Result is ")
        break
    elif decision == "Y":
        print("The Result is ")


