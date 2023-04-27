rows, cols = [int(x) for x in input().split()]

for r in range(rows):
    for c in range(cols):
        print(f"{chr(r + 97)}{chr(r + c + 97)}{chr(r + 97)}", end=" ")

    print()



