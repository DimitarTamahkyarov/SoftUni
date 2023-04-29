lists = [string.split() for string in input().split("|")]

result = []

for _ in range(len(lists)):
    result.extend(lists.pop())

print(*result)