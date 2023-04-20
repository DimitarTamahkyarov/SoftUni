n = int(input())
names = set(input() for _ in range(n))
print(*names, sep="\n")

# print(*{input() for _ in range(int(input()))}, sep="\n")

