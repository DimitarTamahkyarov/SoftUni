from collections import deque
def color_check(color, colors_list):
    result = False
    if color in ["red", "yellow", "blue", "orange", "purple", "green"]:
        colors_list.append(color)
        result = True

    return result

sub_strings = deque(input().split())
colors = []
second_colors = []

while len(sub_strings) > 1:
    left = sub_strings.popleft()
    right = sub_strings.pop()
    combination = left + right
    second_combination = right + left

    if color_check(combination, colors) or color_check(second_combination, colors):
        pass
    else:
        left = left[:-1]
        right = right[:-1]
        if right:
            sub_strings.insert(len(sub_strings)//2, right)
        if left:
            sub_strings.insert(len(sub_strings) // 2, left)

color_check(sub_strings.pop(), colors) if sub_strings else None

colors.remove("orange") if "orange" in colors and ("red" not in colors or "yellow" not in colors) else None
colors.remove("purple") if "purple" in colors and ("red" not in colors or "blue" not in colors) else None
colors.remove("green") if "green" in colors and ("blue" not in colors or "yellow" not in colors) else None

print(colors)
