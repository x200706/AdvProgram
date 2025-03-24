num = int(input())
for _ in range(num):
    sub_num = int(input().split()[2])
    arr = []
    for __ in range(sub_num):
        line = list(map(int, input().split()))
        arr.extend(line)
    flag = True
    reversed_arr = list(reversed(arr))
    for i in range(len(arr)):
        if (arr[i] != reversed_arr[i]) or (reversed_arr[i] < 0 ):
            flag = False
            break
    if flag == True:
        print(f' Test #{_ + 1}: Symmetric.')
    else:
        print(f' Test #{_ + 1}: Non-Symmetric.')