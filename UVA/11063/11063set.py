I = 1

while True:
    try:
        line = input()
        if not line:
            print()
            continue
        n = int(line)
        arr = list(map(int, input().split()))

        flag = True
        # 條件一：數列前項小於等於後項
        for i in range(n - 1):
            if arr[i] >= arr[i + 1] or arr[i] < 1:
                flag = False
                break
        if not flag:
            ans = 'It is not a B2-Sequence.'
            print(f'Case #{I}: {ans}')
            I += 1
            continue

        # 條件二：所有相加的可能不能出現一樣的數字
        cal_arr = set()
        for i in range(n):
            for j in range(i, n):
                su = arr[i] + arr[j]
                if su in cal_arr:
                    flag = False
                    break
                cal_arr.add(su)
            if not flag:
                break

        ans = 'It is a B2-Sequence.' if flag else 'It is not a B2-Sequence.'
        print(f'Case #{I}: {ans}') 
        I += 1
    except EOFError:
        break