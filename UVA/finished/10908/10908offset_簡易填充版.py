num = int(input())
for _ in range(num):
    h, w, test = map(int, input().split())
    print(f'{h} {w} {test}')
    
    arr = []

    for i in range(h):
        line_arr = list(input())
        arr.append(line_arr)

    for i in range(test):
        x, y = map(int, input().split())
        up, left, down, right = x - 0, y - 0, h - 1 - x, w - 1 - y
        max_side = 1 + 2 * min(up, left, down, right)

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
                    
