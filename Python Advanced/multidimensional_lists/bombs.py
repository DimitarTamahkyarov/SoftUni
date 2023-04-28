n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = input().split()

for bomb in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb.split(",")]
    bomb_power = matrix[bomb_row][bomb_col]
    if bomb_power <= 0:
        continue
    bomb_row_range = range(bomb_row - 1, bomb_row + 2)
    bomb_col_range = range(bomb_col - 1, bomb_col + 2)

    for r in bomb_row_range:
        for c in bomb_col_range:
            if 0 <= r < n and 0 <= c < n:
                if matrix[r][c] > 0:
                    matrix[r][c] -= bomb_power

alive_cells_count = 0
sum_alives_cells = 0

for r in matrix:
    sum_alives_cells += sum([el for el in r if el > 0])
    alive_cells_count += len([el for el in r if el > 0])

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {sum_alives_cells}")
for row in matrix:
    print(*row)
