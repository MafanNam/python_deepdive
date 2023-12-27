import math


def f(x):
    return 1 / math.sqrt(x ** 2 + 1)


# Left rectangle method
def left_s(a, b, n):
    s = 0
    h = (b - a) / float(n)
    for i in range(n):
        s += f(a + i * h)
    s *= h
    return s


# Right rectangle method
def right_s(a, b, n):
    s = 0
    h = (b - a) / float(n)
    for i in range(1, n + 1):
        s += f(a + i * h)
    s *= h
    return s


# Midpoint rectangle method
def mid_s(a, b, n):
    s = 0
    h = (b - a) / float(n)
    for i in range(n):
        s += f(a + (i + 0.5) * h)
    s *= h
    return s


if __name__ == "__main__":
    a = float(input("a = "))
    b = float(input("b = "))
    n = int(input("Enter the number of division segments n = "))

    print("\nThe method of rectangles")
    print(f"Integration of a function f(x) = 1/math.sqrt(x + 2.5) on the interval [{a}; {b}]")

    print("\nWith method of left-hand rectangles:")
    print(f"S = {left_s(a, b, n):.4f}")

    print("\nWith method of right-hand rectangles:")
    print(f"S = {right_s(a, b, n):.4f}")

    print("\nWith mid-square method:")
    print(f"S = {mid_s(a, b, n):.4f}")

import math


def f(x):
    return math.cos(x) / (x + 2)


def simpsons_method(a, b, n):
    s = 0
    s1 = 0
    s2 = 0
    h = (b - a) / float(n)
    x = a + h

    for i in range(1, n, 2):
        s1 += f(x)
        x += 2 * h

    x = a + 2 * h
    for i in range(2, n, 2):
        s2 += f(x)
        x += 2 * h

    s += f(a) + f(b) + 4 * s1 + 2 * s2
    s *= h / 3

    return s


if __name__ == "__main__":
    a = float(input("a = "))
    b = float(input("b = "))
    n = int(input("Enter the number of division segments n = "))

    print("\nThe Simpson's method")
    print(f"Integration of a function (x**2+1) math.sin(x-0.5) on the interval [{a}; {b}]")

    result = simpsons_method(a, b, n)
    print(f"With Simpson's method, S = {result:.2f}")

import math


def f(x):
    return 1 / math.sqrt(x ** 2 - 3)


def trapezoidal_method(a, b, n):
    s = 0
    h = (b - a) / float(n)
    x = a

    for i in range(1, n):
        x += h
        s += f(x)

    s += f(a) / 2 + f(b) / 2
    s *= h

    return s


if __name__ == "__main__":
    a = float(input("a = "))
    b = float(input("b = "))
    n = int(input("Enter the number of division segments n = "))

    print("\nThe method of trapezoids")
    print(f"Integration of a function f(x) = 1 / math.sqrt(x**2+4) on the interval [{a}; {b}]")

    result = trapezoidal_method(a, b, n)
    print(f"With the trapezoidal method, S = {result:.4f}")
