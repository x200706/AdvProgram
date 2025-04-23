import math
while True:
    try:
        line = input().split()
        s = float(line[0])
        a = float(line[1])
        kind = line[2]
        r = s + 6440

        if kind == 'min':
            a = a / 60 # 已經是浮點不用再轉一次了

        if a > 180:
            a = abs(360-a)
        
        # 轉成弧度
        theta = a * math.pi / 180

        arc = r * theta
        chord = 2 * r * math.sin(theta / 2)

        print(f"{arc:.6f} {chord:.6f}")

    except EOFError:
        break
