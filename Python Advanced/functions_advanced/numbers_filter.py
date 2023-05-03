def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == "even":
            kwargs[k] = [num for num in v if num % 2 == 0]
        else:
            kwargs[k] = [num for num in v if num % 2 == 1]

    return dict(sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
