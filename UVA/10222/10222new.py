kb = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
kb_arr = list(kb)

while True:
    try:
        line_arr = list(input())
        for i in range(len(line_arr)):
            e = line_arr[i].lower()
            if e in kb_arr:
                ori_index = kb_arr.index(e)
                print(kb_arr[ori_index - 2], end = '')
            else:
                print(' ', end = '')
        print()

    except EOFError:
        break