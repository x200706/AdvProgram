temp_arr = []
max_len = 0 # 原本的i 處理後會變成新陣列j  
line_num = 0 # 原本的j 處理後會變成新陣列i

def rolate(max_len, line_num, arr):
    # 要正確初始化新陣列避免index out of range
    new_arr = [['' for _ in range(line_num)] for _ in range(max_len)] # Python初始化陣列更正確的方式...
    
    for i in range(max_len):  # 遍歷每一列
        for e in reversed(arr):  # 從下往上遍歷每一行
            if i < len(e):
                new_arr[i].append(e[i])
            else:
                new_arr[i].append(' ')
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
        line_num += 1
    except EOFError:
        break

new_arr = rolate(max_len, line_num, temp_arr)
for i in range(len(new_arr)):
    print(''.join(new_arr[i]).rstrip())
#TODO 我測試tab也行啊 好奇怪啊