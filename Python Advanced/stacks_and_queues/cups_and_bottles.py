from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = [int(bottle) for bottle in input().split()]
wasted_water = 0

while cups and bottles:
    next_bottle = bottles.pop()

    if cups[0] <= next_bottle:
        wasted_water += next_bottle - cups.popleft()
    else:
        cups[0] -= next_bottle

if not cups:
    print(f"Bottles:", end=" ")
    for bottle in bottles:
        print(bottle, end=" ")

if not bottles:
    print(f"Cups:", end=" ")
    for cup in cups:
        print(cup, end=" ")

print(f"\nWasted litters of water: {wasted_water}")