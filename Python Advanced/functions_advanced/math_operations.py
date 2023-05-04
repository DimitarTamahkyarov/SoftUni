def math_operations(*nums, **kwargs):
    counter = 1
    for num in nums:
        if counter == 1:
            kwargs["a"] += num
        elif counter == 2:
            kwargs["s"] -= num
        elif counter == 3 and num != 0:
            kwargs["d"] /= num
        elif counter == 4:
            kwargs["m"] *= num
            counter = 0
        counter += 1

    result = [f"{k}: {v:.1f}" for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))