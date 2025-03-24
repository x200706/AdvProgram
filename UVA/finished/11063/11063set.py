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
        if arr[0] < 1 or any(arr[i] <= arr[i - 1] for i in range(1, n)):  
            print(f"Case #{I}: It is not a B2-Sequence.")
            I += 1
            continue

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

        ans = 'It is a B2-Sequence.' if flag else 'It is not a B2-Sequence.'
        print(f'Case #{I}: {ans}') 
        I += 1
    except EOFError:
        break