table = {}  # 在這邊才不會被重置
while True:
    try:
        a, b = map(int, input().split()) # 用arr容易超過記憶體..
        # 小心如果宣告一個ori_arr = line_arr時，line_arr.sort() ori_arr的順序也會被改變X_X
        # 使用sort數組一大就會卡一下欸
        original_a, original_b = a, b # 一直用max() min() 也會用太多記憶體
        if a > b:
            a, b = b, a
        max_time = 0
        time = 0
        for i in range(a, b + 1):
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
            if time > max_time:
                max_time = time
        print(f'{original_a} {original_b} {max_time}')
    except EOFError:
        break

# 參考
# https://blog.iddle.dev/public/2023/03/19/Python-UVa-100-The-3n-1-problem/#google_vignette 無遞迴解