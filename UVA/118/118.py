while True:
    try:
        X, Y = map(int, input().split())
        scent = [[False] * (Y + 1) for _ in range(X + 1)]  # 僅記錄位置
        directions = ['N', 'E', 'S', 'W']
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        while True:
            line = input().strip()
            if not line:
                break
            x, y, dir = line.split()
            x, y = int(x), int(y)
            if dir not in directions or x < 0 or x > X or y < 0 or y > Y:
                input()  # 讀取指令行並跳過
                continue
            commands = input().strip()
            
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
                    if nx < 0 or nx > X or ny < 0 or ny > Y:
                        if not scent[x][y]: 
                            scent[x][y] = True
                            lost = True
                    else:
                        x, y = nx, ny
            
            print(f"{x} {y} {directions[d]}", end="")
            if lost:
                print(" LOST")
            else:
                print()
                
    except EOFError:
        break