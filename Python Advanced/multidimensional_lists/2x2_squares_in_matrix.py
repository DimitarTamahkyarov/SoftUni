rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for row in range(rows)]
finded = 0

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row + 1][col] == matrix[row + 1][col + 1] == matrix[row][col + 1]:
            finded += 1

print(finded)