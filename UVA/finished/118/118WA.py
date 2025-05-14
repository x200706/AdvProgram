while True:
    try:
        X, Y = map(int, input().split())
        
        # scent[x][y][dir]
        scent = [[[False] * 4 for _ in range(Y + 1)] for _ in range(X + 1)]

        directions = ['N', 'E', 'S', 'W']

        # 前進時的座標變化
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        while True:
            line = input().strip()
            if not line:
                break
            x, y, dir = line.split()
            x, y = int(x), int(y)
            commands = input().strip()
            
            if dir not in directions:
                continue
            d = directions.index(dir)
            lost = False
            
            for cmd in commands:
                if lost:
                    break 
                if cmd == 'L':
                    d = (d - 1) % 4
                elif cmd == 'R':
                    d = (d + 1) % 4
                elif cmd == 'F':
                    nx, ny = x + dx[d], y + dy[d]
                    # 檢查是否超出邊界
                    if nx < 0 or nx > X or ny < 0 or ny > Y:
                        # 檢查是否有氣味
                        if not scent[x][y][d]:
                            scent[x][y][d] = True  # 標記氣味
                            lost = True  # 標記為 LOST
                    else:
                        x, y = nx, ny
                else:
                    continue
            
            # 輸出結果
            print(f"{x} {y} {directions[d]}", end="")
            if lost:
                print(" LOST")
            else:
                print()
                
    except EOFError:
        break