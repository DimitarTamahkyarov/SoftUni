def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes = 0

    for arg in args:
        if arg != "Finish":
            cubes += arg
        else:
            break

    if volume >= cubes:
        return f"There is free space in the box. You could put {volume-cubes} more cubes."
    else:
        return f"No more free space! You have {cubes-volume} more cubes."

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))