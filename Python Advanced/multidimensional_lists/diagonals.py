matrix_size = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(matrix_size)]

main_diagonal = [matrix[i][i] for i in range(matrix_size)]
secondary_diagonal = [matrix[i][matrix_size-1-i] for i in range(matrix_size)]

print(f"Primary diagonal: {', '.join(str(el) for el in main_diagonal)}. Sum: {sum(main_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
