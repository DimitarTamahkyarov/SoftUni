def cache(func):

    def wrapper(num):
        if num not in wrapper.log:
            wrapper.log[num] = func(num)

        return wrapper.log[num]

    wrapper.log = {0: 0, 1: 1}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(3)
print(fibonacci.log)
