n = int(input())
for I in range(n):
    arr = []
    matrix_n = int(list(input().split())[2])
    flag = True 
    for i in range(matrix_n):
        arr.extend(list(map(int, input().split()))) # https://blog.csdn.net/m0_51713294/article/details/112389296
    reversed_arr = list(reversed(arr))


    # 不用巢狀迴圈啦 亂跑一通@@|||...
    for i in range(len(arr)):
        #HINT 題目只接受元素為非負數陣列
        if (arr[i] != reversed_arr[i]) or (arr[i] < 0) or (reversed_arr[i] < 0):
            flag = False
            break

    if flag is True:
        ans = 'Symmetric'
    else:
        ans = 'Non-symmetric'
    print(f'Test #{I + 1}: {ans}.')