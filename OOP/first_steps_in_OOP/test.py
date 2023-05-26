x = "Global"

def some_func():
    x = "non global"
    return x

print(some_func())