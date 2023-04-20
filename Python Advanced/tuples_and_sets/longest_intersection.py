longest_intersection = []

for _ in range(int(input())):
    first, second = [[int(n) for n in el.split(",")] for el in input().split("-")]
    intersection = set(range(first[0], first[1]+1)) & set(range(second[0], second[1]+1))
    longest_intersection = intersection if len(intersection) > len(longest_intersection) else longest_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")