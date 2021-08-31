import math

def main():
    inpt = input("a = ")
    validate_param(inpt)
    a = int(inpt)
    print(a)

    inpt = input("b = ")
    validate_param(inpt)
    b = int(inpt)
    print(b)

    inpt = input("c = ")
    validate_param(inpt)
    c = int(inpt)
    print(c)

    roots = solve_square(a,b,c)
    square_print(a,b,c,roots)



def validate_param(inpt):
    i=0
    while i < 3:
        try:
            return int(inpt)
        except ValueError:
            inpt = input("Please, enter numeric value: ")
            i+=1

def discriminant(a,b,c):
    d = b ** 2 - 4 * a * c
    print("Discriminant D = %.2f" % d)
    return d

def roots(d:int,a:int,b:int,c:int) -> tuple:
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return (x1,x2)
    elif d == 0:
        x1 = -b / (2 * a)
        return (x1)
    else:
        print("No roots")

def solve_square(a,b,c):
    a,b,c
    d = discriminant(a,b,c)
    return roots(d,a,b,c)

def square_print(a,b,c,roots):
    print(a,b,c,roots)

main()