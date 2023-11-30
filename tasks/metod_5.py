from sympy import *

# Input the expression
equation = input("Enter the expression: ")

# Calculate the first and second derivatives
yy = diff(equation)
yyy = diff(yy)

# Find the roots of the first derivative
Roots = [i for i in solve(yy) if i.is_real]

print('Roots:', Roots)

# Extend the roots to create intervals
a1 = min(Roots) - 1
b1 = max(Roots) + 1
Roots.extend([b1, a1])

print('Extended Roots:', Roots)

# Find the interval for the first root
while True:
    if (simplify(equation).evalf(subs={"x": a1}) > 0 and simplify(equation).evalf(subs={"x": b1}) < 0) or (
            simplify(equation).evalf(subs={"x": a1}) < 0 and simplify(equation).evalf(subs={"x": b1}) > 0):
        break
    else:
        a1 -= 1
        b1 -= 1

print("Interval for the first root:", "[", a1, ";", b1, "]")

# Find the interval for the second root
a2 = min(Roots)
b2 = max(Roots) + 1

while True:
    if (simplify(equation).evalf(subs={"x": a2}) > 0 and simplify(equation).evalf(subs={"x": b2}) < 0) or (
            simplify(equation).evalf(subs={"x": a2}) < 0 and simplify(equation).evalf(subs={"x": b2}) > 0):
        break
    else:
        a2 += 1
        b2 += 1

print("Interval for the second root:", "[", a2, ";", b2, "]")

# Apply Newton's method to find the first root
xn = a1
while True:
    fy = simplify(equation).evalf(subs={"x": xn})
    fyy = simplify(yy).evalf(subs={"x": xn})
    xn1 = xn - (fy / fyy)
    fy1 = simplify(equation).evalf(subs={"x": xn1})
    fyy1 = simplify(yy).evalf(subs={"x": xn1})
    dif = abs(xn1 - xn)
    if dif < 0.000001:
        break
    else:
        xn = xn1

print("First root (Newton's method):", round(xn1, 6))

# Apply the bisection method to find the second root
an = a2
bn = b2
while True:
    xn = (an + bn) / 2
    fy = simplify(equation).evalf(subs={"x": xn})
    dif = abs(an - bn)
    if dif < 0.000002:
        break
    else:
        if simplify(equation).evalf(subs={"x": xn}) < 0:
            an = xn
        elif simplify(equation).evalf(subs={"x": xn}) > 0:
            bn = xn

print("Second root (Bisection method):", round(xn, 6))
