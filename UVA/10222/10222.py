kb = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
kb_arr = list(kb)

while True:
    try:
        line_arr = list(input())
        ans = ''
        for e in line_arr: 
            e = e.lower()
            if e in kb_arr:
                original_index = kb_arr.index(e)
                ans += kb_arr[original_index - 2]
            else:
                ans += ' '
        print(ans)
    except EOFError:
        break