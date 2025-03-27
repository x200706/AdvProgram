while True:
    try:
        s = input()
        if not s:
            break

        total = 0
        max_digit = 0
        for char in s: # 就是定義，不要想太多
            if '0' <= char <= '9':
                value = ord(char) - ord('0')  # 0-9
            elif 'A' <= char <= 'Z':
                value = ord(char) - ord('A') + 10  # 10-35
            elif 'a' <= char <= 'z':
                value = ord(char) - ord('a') + 36  # 36-61
            else:
                continue  # 忽略無效字符
            total += value
            max_digit = max(max_digit, value)

        # 最小的有效基數是 2
        if max_digit == 0 and total == 0:
            print(2)  # 最小的有效基數是 2
            continue

        min_base = max_digit + 1
        found = False
        for n in range(min_base, 63):  # n 
            if total % (n - 1) == 0:  # 同餘定理："位數和" 能被 "n-1"整除
                print(n)
                found = True
                break
        
        if not found:
            print("such number is impossible!")
    except EOFError:
        break