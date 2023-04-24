from collections import deque
from functools import reduce

expression = deque(input().split())
temp = deque()

function = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b
}

while len(expression) > 1:
    element = expression.popleft()

    if str(element) in "*/+-":
        expression.appendleft(reduce(function[element], temp))
        temp.clear()
    else:
        temp.append(int(element))
expression.appendleft(reduce(function[expression.popleft()], temp))

print(*expression)
