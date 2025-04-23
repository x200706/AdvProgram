num = int(input())
for _ in range(num):
    h, w, unit = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    print(f'{h} {w} {unit}')
    
    for _ in range(unit):
        x, y = map(int, input().split())

        # 計算最大可能邊長
        u, l, d, r = x, y, h - 1 - x, w - 1 - y
        max_side = 2 * min(u, l, d, r) + 1  # 最大可能的奇數邊長
        
        result = 1 
        # 嘗試所有可能的奇數邊長
        for side in range(1, max_side + 1, 2):
            valid = True
            half_side = side // 2
            # 檢查正方形區域
            for i in range(x - half_side, x + half_side + 1):
                for j in range(y - half_side, y + half_side + 1):
                    # 確保不越界且char匹配
                    if i < 0 or i >= h or j < 0 or j >= w or arr[i][j] != arr[x][y]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                result = side
            else:
                break 
        
        print(result)