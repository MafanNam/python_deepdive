import math

print("T1\n")


# Функція для обчислення відносної похибки dx
def dxFunc(x, X):
    """dx = |x - X|/x"""
    return abs(x - X) / x


n1, x1 = 9.8, 3.13
X1 = math.sqrt(n1)
dx1 = dxFunc(x1, X1)

n2, N2, x2 = 23, 15, 1.53
X2 = n2 / N2
dx2 = dxFunc(x2, X2)

print(f"√{n1} = {x1} or {n2}/{N2} = {x2}")
print(f"dx1 = {round(dx1, 4)}, ({round(dx1 * 100, 2)}%)")
print(f"dx2 = {round(dx2, 4)}, ({round(dx2 * 100, 2)}%)")

print(f"sqrt({n1}) is more accurate" if dx1 < dx2 else f"{n2}/{N2} is more accurate")

# T2
print("\nT2(a)\n")

x, dx, a, i = 8.3445, 0.0022, 0.005, 0

# Визначення кількості знаків після коми для округлення
while dx < a / 10:
    a /= 10
    i += 1

fdx = round(dx + abs(round(x, i) - x), 4)

# Знаходження "найточніших" чисел
while fdx > a:
    i -= 1
    a *= 10
    tmp = abs(round(x, i))
    fdx = round(dx + abs(round(x, i) - x), 4)

print(f"Since ∆x** < 0.005, the remaining numbers in the rounded number x={round(fdx, 1)} are true in the narrow sense")

print("\nT2(b)\n")

x, sx = 23.574, 0.02  # 0.2%

# Обчислення похибки dx та "найточніших" чисел
dx, er, i = x * sx / 100, 1, 0
if x > 9:
    i -= 1
while dx < er:
    er /= 10
    i += 1
er *= 10

ndx = dx + abs(round(x, i) - x)  # ∆x*

# Знаходження "найточніших" чисел
while ndx < er:
    i -= 1
    ndx = dx + abs(round(x, i) - x)  # ∆x* = ∆x + |x* - x|

print(f"Since ∆x** < 0.1, the remaining numbers in the rounded number x={round(x, i)} are true in the narrow sense")

# T3
print("\nT3(a)\n")

x = 20.43
x2, i = x, 0

# Визначення кількості знаків після коми для округлення
while int(x2) != x:
    i += 1
    x, x2 = x * 10, x2 * 10
    x, x2 = round(x, 7), round(x2, 7)

x /= 10 ** i
dx = (0.1 / (10 ** i)) * 5  # ∆x
sx = dx / x  # σx
print(f"∆x = {dx}, σx = {round(sx, 5)} ({round(sx * 100, 3)}%)")

print("\nT3(b)\n")

x = 0.576
x2, i = x, -1

# Визначення кількості знаків після коми для округлення
while int(x2) != x:
    i += 1
    x, x2 = x * 10, x2 * 10
    x, x2 = round(x, 7), round(x2, 7)

x /= 10 ** (i + 1)
dx = 0.1 / (10 ** i)  # ∆x
sx = dx / x  # σx
print(f"∆x = {dx}, σx = {round(sx, 3)} ({round(sx * 100, 1)}%)")
