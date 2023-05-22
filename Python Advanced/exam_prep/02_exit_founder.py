from collections import deque

player_one, next_player = input().split(", ")

matrix = [input().split() for row in range(6)]

players_hit_the_wall = deque()

while True:
    row, col = [int(num) for num in input()[1:-1].split(", ")]

    if players_hit_the_wall:
        if players_hit_the_wall[0] == player_one:
            players_hit_the_wall.popleft()
            player_one, next_player = next_player, player_one
            continue

    if matrix[row][col] == "E":
        print(f"{player_one} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        print(f"{player_one} is out of the game! The winner is {next_player}.")
        break
    elif matrix[row][col] == "W":
        print(f"{player_one} hits a wall and needs to rest.")
        players_hit_the_wall.append(player_one)

    player_one, next_player = next_player, player_one
