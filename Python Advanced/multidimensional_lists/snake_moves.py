from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())

for r in range(rows):
    curr_row = deque()
    for c in range(cols):
        curr_char = snake.popleft()
        if r % 2 == 0:
            curr_row.append(curr_char)
        else:
            curr_row.appendleft(curr_char)
        snake.append(curr_char)
    print(*curr_row, sep="")
    curr_row.clear()

