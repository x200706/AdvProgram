count = 1

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
        if arr[0] < 1 or any(arr[i] <= arr[i - 1] for i in range(1, n)):  
            print(f"Case #{count}: countt is not a B2-Sequence.")
            count += 1
            continue

        # 條件二：所有相加的可能不能出現一樣的數字
        cal_set = set()
        for i in range(n):
            for j in range(i, n):
                su = arr[i] + arr[j]
                if su in cal_set:
                    flag = False
                    break
                cal_set.add(su)
            if not flag:
                break

        ans = 'countt is a B2-Sequence.' if flag else 'countt is not a B2-Sequence.'
        print(f'Case #{count}: {ans}') 
        count += 1
    except EOFError:
        break