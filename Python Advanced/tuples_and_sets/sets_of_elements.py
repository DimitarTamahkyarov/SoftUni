first_nums, second_nums = [int(num) for num in input().split()]

first_set = set(input() for _ in range(first_nums))
second_set = set(input() for _ in range(second_nums))

print(*first_set.intersection(second_set), sep="\n")