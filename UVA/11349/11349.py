n = int(input())
for I in range(n):
    arr = []
    ma_n = int(list(input().split())[2])
    for i in range(ma_n):
        arr.extend(list(map(int, input().split()))) # https://blog.csdn.net/m0_51713294/article/details/112389296
    flag = True

    for e in arr:
        for r_e in list(reversed(arr)):
            print(f'{e} {r_e}')
            if e != r_e: # 這附近代碼怪怪的
                flag = False
                break

    if flag is True:
        ans = 'Symmetric'
    else:
        ans = 'Non-symmetric'
    print(f'Test #{I + 1}: {ans}.')