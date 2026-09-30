import math

a = 0.5
b = 0.9
h = 0.05
d = 0.001

x = a
while x <= b + 1e-9:
    s = x
    n = 1
    term = (1 / 2) * (x**3 / 3)

    while abs(term) >= d:
        s += term
        n += 1
        term = term * ((2 * n - 3) / (2 * n - 2)) * ((2 * n - 3) / (2 * n - 1)) * (x**2)

    print(f"{x:.2f} {s:.5f} {n}")
    x += h