chemicals = set()

for _ in range(int(input())):
    chemicals = chemicals | set(input().split())

print(*chemicals, sep="\n")
