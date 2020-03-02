def add(a, b):
    print(f'ADDING {a!r} {b!r}')
    return a + b


def subtract(a, b):
    print(f'SUBSTRACTING {a!r} {b!r}')
    return a - b


def multiply(a, b):
    print(f'multiplying {a!r} {b!r}')
    return a * b


def divide(a, b):
    print(f'divide {a!r} {b!r}')
    return a / b


print(f'Let\'s do some math')
age = add(30, 5)  # 35
height = subtract(78, 4)  # 74
weight = multiply(90, 2)  # 180
iq = divide(100, 2)  # 50


what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# -4426
print(what)


