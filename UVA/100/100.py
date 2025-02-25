table = {}  # 在這邊才不會被重置
while True:
    try:
        line_arr = list(map(int, input().split()))
        a = line_arr[0]
        b = line_arr[1] # 小心如果宣告一個ori_arr = line_arr時，line_arr.sort() ori_arr的順序也會被改變X_X
        # 使用sort數組一大就會卡一下欸
        max_time = 0
        time = 0
        for i in range(min(a, b), max(a, b) + 1):
            n_for_deal = i
            time = 0
            while True:
                if n_for_deal in table: # 如果計算過了
                    time += table[n_for_deal]
                    break
                
                time += 1
                if n_for_deal == 1:
                    break
                if n_for_deal % 2 == 0:
                    n_for_deal = n_for_deal // 2
                else:
                    n_for_deal = 3 * n_for_deal + 1
            table[i] = time
            max_time = max(time, max_time)
        print(f'{a} {b} {max_time}')
    except EOFError:
        break

# 參考
# https://blog.iddle.dev/public/2023/03/19/Python-UVa-100-The-3n-1-problem/#google_vignette 無遞迴解