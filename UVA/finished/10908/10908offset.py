num = int(input())
for _ in range(num):
    h, w, unit = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    print(f'{h} {w} {unit}')
    
    for _ in range(unit):
        x, y = map(int, input().split())
        u, l, d, r = x, y, h - 1 - x, w - 1 - y
        max_side = 2 * min(u, l, d, r) + 1
        
        result = 1
        for side in range(1, max_side + 1, 2):
            valid = True
            offset = (side - 1) // 2
            for i in range(x - offset, x + offset + 1):
                for j in range(y - offset, y + offset + 1):
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