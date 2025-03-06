# 這題訓練圖像思考..
temp_arr = []
max_len = 0 # 原本的i 處理後會變成新陣列j  
line_num = 0 # 原本的j 處理後會變成新陣列i

def rolate(max_len, line_num, arr):
    # 要正確初始化新陣列避免index out of range
    new_arr = [[] * line_num for _ in range(max_len)]
    for i in range(line_num): # 0~1
        for j in reversed(range(max_len)): # 25~0
            if j >= len(arr[i]):
                new_arr[j].append(' ')
            else:
                new_arr[j].insert(0, arr[i][j])
    return new_arr

while True:
    try:
        line = input()
        if line == '':  # 如果輸入是空行，跳過
            continue
        line_arr = list(line)
        temp_arr.append(line_arr)
        if len(line_arr) > max_len:
            max_len = len(line_arr)
        line_num += 1 # 原本的j 會變成i
    except:
        break

new_arr = rolate(max_len, line_num, temp_arr)
for i in range(len(new_arr)):
    print(''.join(new_arr[i]).rstrip())
# 是說Python程式有問題也不一定會拋例外欸......