even_set = set()
odd_set = set()

for n in range(1, int(input())+1):
    sum_of_chars = sum(ord(char) for char in input()) // n

    if sum_of_chars % 2 == 0:
        even_set.add(sum_of_chars)
    else:
        odd_set.add(sum_of_chars)

if sum(even_set) < sum(odd_set):
    print(*(odd_set - even_set), sep=", ")
elif sum(even_set) > sum(odd_set):
    print(*(even_set ^ odd_set), sep=", ")
else:
    print(*(even_set & odd_set), sep=", ")