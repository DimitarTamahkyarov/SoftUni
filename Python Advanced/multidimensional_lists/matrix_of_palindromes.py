rows, cols = [int(x) for x in input().split()]

matrix = []

for r in range(rows):
    matrix.append([])
    for c in range(cols):
        palindrome = f"{chr(r + 97)}{chr(r + c + 97)}{chr(r + 97)}"
        matrix[r].append(palindrome)

for row in matrix:
    print(*row)
