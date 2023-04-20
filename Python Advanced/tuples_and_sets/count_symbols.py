text = input()

print(*sorted(set(f"{char}: {text.count(char)} time/s" for char in text)), sep="\n")