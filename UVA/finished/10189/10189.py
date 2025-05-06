def count_mines(grid, row, col, rows, cols):
    diff = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for x, y in diff:
        new_row, new_col = row + x, col + y
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '*':
                count += 1
    return count

case = 0
while True:
    try:
        line = input().strip()
        if not line:
            continue
        rows, cols = map(int, line.split())
        if rows == 0 and cols == 0:
            break
        case += 1
        
        grid = [list(input().strip()) for _ in range(rows)]

        # 初始化結果陣列
        result = [['0' for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    result[i][j] = '*'
                else:
                    result[i][j] = str(count_mines(grid, i, j, rows, cols))
        
        if case > 1:
            print()
        print(f"Field #{case}:")
        for row in result:
            print(''.join(row))
    except EOFError:
        break