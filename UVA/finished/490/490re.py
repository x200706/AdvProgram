str_collect_arr = []
max_len = 0

def solve(arr, le):
    for i in range(le + 1):
        for e in reversed(arr):
            try:
                print(e[i], end = '')
            except:
                print(' ', end = '')
        print()


while True:
    try:
        line_arr = list(input())
        str_collect_arr.append(line_arr)
        if len(line_arr) > max_len:
            max_len = len(line_arr)
    except EOFError:
        break

solve(str_collect_arr, max_len)
# 受到大大的啟發 https://github.com/yuusukealmal/CPE/blob/main/CPE49/UVA490.py