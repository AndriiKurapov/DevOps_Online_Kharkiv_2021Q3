import math


def main():
    inpt = input("a = ")
    a = validate_param(inpt)

    inpt = input("b = ")
    b = validate_param(inpt)

    inpt = input("c = ")
    c = validate_param(inpt)

    roots = solve_square(a, b, c)
    square_print(a, b, c, roots)


def validate_param(inpt):
    i = 0
    while i < 2:
        try:
            return int(inpt)
        except ValueError:
            inpt = input("Try integer: ")
            i += 1
    exit(1)


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    print("Discriminant = %i" % d)
    return d


def roots(d, a, b, c):
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(x1, x2)
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        print(x1)
        return x1
    else:
        print("This equation has no roots")


def solve_square(a, b, c):
    d = discriminant(a, b, c)
    return roots(d, a, b, c)


def square_print(a, b, c, roots):
    print(a, b, c, roots)

