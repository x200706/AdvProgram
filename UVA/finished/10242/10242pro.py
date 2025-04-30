def find_final_point(x1, y1, x2, y2, x3, y3):
    return x1 + x3 - x2, y1 + y3 - y2

while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
        points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        
        # 找出重複的點
        common = None
        for i in range(4):
            for j in range(i + 1, 4):
                if points[i] == points[j]:
                    common = points[i]
                    break
            if common:
                break
        
        # 找出另外兩個點
        others = [p for p in points if p != common]
        
        # 第四點公式：D = A + C - B
        px, py = find_final_point(others[0][0], others[0][1], common[0], common[1], others[1][0], others[1][1])
        
        print(f"{px:.3f} {py:.3f}")
    except EOFError:
        break