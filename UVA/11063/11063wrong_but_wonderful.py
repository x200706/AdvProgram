count = 1
while True:
    try:
        flag = True
        line = input()
        if not line:
            print()
            continue
        l = int(line)
        arr = list(map(int, input().split()))

        if arr[0] < 1 or any(arr[i] <= arr[i - 1] for i in range(1, l)):
            print(f"Case #{count}: It is not a B2-Sequence.")
            count += 1
            continue

        output_arr = set()
        for i in range(l):
            for j in range(i, l):
                temp_sum = arr[i] + arr[j]
                if temp_sum in output_arr:
                    flag = False
                    break
                output_arr.add(temp_sum)
            if not flag:
                break

        if flag == True:
            print(f' Case #{count}: It is a B2-Sequence.')
        else:
            print(f' Case #{count}: It is not a B2-Sequence')
        count += 1
    except EOFError:
        break