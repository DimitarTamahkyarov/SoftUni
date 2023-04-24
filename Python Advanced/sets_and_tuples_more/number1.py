first = set(int(num) for num in input().split())
second = set(int(num) for num in input().split())

functions = {
    "Add First": lambda x: [first.add(int(num)) for num in x],
    "Add Second": lambda x: [second.add(int(num)) for num in x],
    "Remove First": lambda x: [first.discard(num) for num in new_nums],
    "Remove Second": lambda x: [second.discard(num) for num in new_nums],
    "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)
}

for _ in range(int(input())):
    info, *new_nums = input().split()
    command = f"{info} {new_nums.pop(0)}"

    functions[command](new_nums) if new_nums else functions[command]()

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")