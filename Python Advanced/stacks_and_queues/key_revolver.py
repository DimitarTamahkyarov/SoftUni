from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque([int(lock) for lock in input().split()])
intelligence_value = int(input())
curr_barrel = gun_barrel_size
shooted_bullets = 0

while bullets:

    next_bullet = bullets.pop()
    shooted_bullets += 1
    curr_barrel -= 1

    if next_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if curr_barrel == 0 and bullets:
        print("Reloading!")
        curr_barrel = gun_barrel_size

    if not locks:
        money_earned = intelligence_value - shooted_bullets*bullet_price
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")