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
        for i in range(n - 1): #TODO 了解這邊為甚麼錯..
            if (arr[i] >= arr[i + 1]) or (arr[i] < 1): # 總之就是要把題目的數列限制寫成condition
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
                cal_arr.append(su)
            if not flag: # 留意巢狀迴圈退出
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
# 這個解法思維不錯，只是UVA平台不給過 https://github.com/Chen-Wei0107/Collegiate-programming-examination-CPE/blob/ee86d4fd1d03ce3d1fbf2b13c84437160dcc9226/Python%20version%20code/23.UVA11063%20-%20B2-Sequence.py#L4
# 這個解法給過，這個檢查數列條件才是對的，另可以看看Python防禦空行的現象.. https://github.com/ShaoYong-0921/coding-practice/blob/1527228d56c17731fb87b5cc7e578024089b9dd7/UVa_py/UVa11063.py#L4