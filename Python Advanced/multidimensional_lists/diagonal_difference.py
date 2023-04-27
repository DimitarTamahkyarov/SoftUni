matrix_size = int(input())

matrix = [[int(el) for el in input().split()] for row in range(matrix_size)]

main_diagonal = [matrix[i][i] for i in range(matrix_size)]
secondary_diagonal = [matrix[i][matrix_size-1-i] for i in range(matrix_size)]

print(abs(sum(main_diagonal) - sum(secondary_diagonal)))
