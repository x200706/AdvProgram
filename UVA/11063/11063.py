I = 1
while True:
    try:
        line = input()
        if not line:
            print()
            continue
        n = int(line)
        arr = list(map(int, input().split()))
        
        cal_arr = []
        flag = True

        for i in arr:
            for j in arr:
                su = i + j
                if su in cal_arr:
                    flag = False
                    break  # ans怪怪的欸
                cal_arr.append(sum)

        ans = ''
        if flag is True:
            ans = 'It is a B2-Sequence.'
        else:
            ans = 'It is not a B2-Sequence.'
        print(f'Case #{I}: {ans}')
        I += 1
    except EOFError:
        break