while True:
    try:
        line_arr = list(map(int, input().split()))
        n = line_arr[0]

        diff_arr = []
        for i in range(1, n):
            diff_arr.append(abs(line_arr[i] - line_arr[i + 1]))
        diff_arr.sort()

        flag = True
        # print(n) -> 4
        # print(len(diff_arr)) -> 3
        # print(diff_arr) -> [1, 2, 3]
        for i in range(1, n): #HINT 這邊為甚麼是N是個好問題
            # print(i) -> 1 2 3
            if diff_arr[i - 1] != i:
                flag = False
                break

        if flag is True:
            print('Jolly')
        else:
            print('Not Jolly')
    except EOFError:
        break