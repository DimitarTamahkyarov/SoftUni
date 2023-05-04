def grocery_store(**kwargs):
    result = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    def print_result(result = dict):
        print_result = ""
        for k, v in result.items():
            print_result += f"{k}: {v}\n"

        return print_result

    return print_result(result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

