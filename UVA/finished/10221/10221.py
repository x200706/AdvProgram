import math

while True:
    try:
        s, a, input_type = input().split()
        s, a = float(s), float(a)
        r = s + 6440

        # 處理角度
        if input_type == "min":
            a = float(a) / 60 # 角分轉角度
        if a > 180: # 如果角度大於180度，取較短路徑
            a = abs(360 - a)

        # 轉成弧度
        theta = a * math.pi / 180

        arc = r * theta
        chord = 2 * r * math.sin(theta / 2)

        print(f"{arc:.6f} {chord:.6f}")
    except EOFError:
        break