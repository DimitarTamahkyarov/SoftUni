from collections import deque
from datetime import datetime, timedelta

robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()
    product_is_made = False
    for robot, time in robots.items():
        if time[1] == 0 and not product_is_made:
            time[1] = time[0]
            print(f"{robot} - {product} [{factory_time.strftime('%H:%M:%S')}]")
            product_is_made = True
        if time[1] > 0:
            time[1] -= 1
    if not product_is_made:
        products.append(product)


