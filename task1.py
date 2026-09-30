import math

a = 3.0
b = 6.0
h = 0.3

x = a
while x <= b + 1e-9:
    if x < 4.0:
        y = 1 / (math.sin(1 / x) + 4)
    elif 4.0 <= x < 5.0:
        y = x**2 + math.log(x)
    else:
        y = math.tan(abs(x - 3))

    print(f"{x:.2f} {y:.5f}")
    x += h