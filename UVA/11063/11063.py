I = 1
while True:
    try:
        line = input()
        if not line:
            print()
            continue
        n = int(line)
        arr = list(map(int, input().split()))
        flag = True #HINT 旗子不要一直插錯位置rrr
        #HINT 條件一：數列前項小於等於後項
        for i in range(1, n):
            if arr[i - 1] >= arr[i]:
                flag = False
                break
        if flag is False:
            ans = 'It is not a B2-Sequence.'
            print(f'Case #{I}: {ans}')
            I += 1
            continue

        #HINT 條件二：所有相加的可能不能出現一樣的數字
        # 加過的不要再加避免誤判—巢狀迴圈要避免重複計算
        cal_arr = []
        for i in range(n):
            for j in range(i, n):
                su = arr[i] + arr[j]
                if su in cal_arr:
                    flag = False
                    break
                cal_arr.append(su)
            if not flag: # 留意巢狀迴圈跳出..
                break

        ans = ''
        if flag is True:
            ans = 'It is a B2-Sequence.'
        else:
            ans = 'It is not a B2-Sequence.'
        print(f'Case #{I}: {ans}')
        I += 1
    except EOFError:
        break

# 找規律
# 巢狀迴圈對應arr索引號
# 0 0
# 0 1
# 0 2
# 0 3
# 1 1
# 1 2
# 1 3
# 2 2
# 2 3
# 3 3
