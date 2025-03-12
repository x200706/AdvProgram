while True:
    try:
        line_arr = list(map(int, input().split()))
        num = line_arr[0]

        diff_arr = []
        for i in range(num):
            if i == 0:
                continue
            diff_arr.append(abs(line_arr[i] - line_arr[i + 1]))
        diff_arr.sort()

        flag = True

        for i in range(num):
            if i == 0:
                continue
            if diff_arr[i - 1] != i:
                flag = False
                break

        ans = "Jolly" if flag else "Not jolly"
        print(ans)
    except EOFError:
        break