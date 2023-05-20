from collections import deque

caffeine = [int(num) for num in input().split(", ")]
drinks = deque([int(num) for num in input().split(", ")])

max_caffeine = 300
stamat_caffeine = 0

while caffeine and drinks:

    drink = drinks.popleft()
    energy = caffeine.pop() * drink

    if energy + stamat_caffeine > max_caffeine:
        drinks.append(drink)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0
    else:
        stamat_caffeine += energy

if drinks:
    print(f"Drinks left: {', '.join(str(drink) for drink in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")

