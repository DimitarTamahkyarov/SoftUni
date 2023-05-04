def age_assignment(*args, **kwargs):
    result = []
    for char, age in kwargs.items():
        for name in args:
            if name.startswith(char):
                result.append(f"{name} is {age} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))