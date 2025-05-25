import math

cases = int(input())
for _ in range(cases):
    L = int(input())

    # 計算寬度和半徑
    W = 0.6 * L
    r = 0.2 * L

    # 計算面積
    rectangle = L * W
    circle = math.pi * r ** 2

    red = rectangle - circle
    green = circle

    print(f"{green:.2f} {red:.2f}")