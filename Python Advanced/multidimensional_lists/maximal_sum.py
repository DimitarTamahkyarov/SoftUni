import copy

rows, cols = [int(el) for el in input().split()]
matrix = [[int(num) for num in input().split()] for row in range(rows)]
sub_matrix = []
max_sum = float("-inf")

for row in range(rows-2):
    for col in range(cols-2):
        curr_matrix = [
            matrix[row][col: col + 3],
            matrix[row + 1][col: col + 3],
            matrix[row + 2][col: col + 3]
        ]

        curr_sum = sum(curr_matrix[0]) + sum(curr_matrix[1]) + sum(curr_matrix[2])

        if curr_sum > max_sum:
            max_sum = curr_sum
            sub_matrix = copy.deepcopy(curr_matrix)

print(f"Sum = {max_sum}")
for row in sub_matrix:
    print(*row)
