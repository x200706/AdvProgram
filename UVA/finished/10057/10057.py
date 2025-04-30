while True:
    try:
        num = int(input())
        arr = []
        for _ in range(num):
            arr.append(int(input()))
        arr.sort()

        ans1 = 0  # 最小的M
        ans2 = 0  # 接近M的數字數量
        ans3 = 0  # 可能的M數量

        # 分奇數和偶數情況
        if len(arr) % 2 == 1:  # 奇數
            # 中位數
            m_index = len(arr) // 2
            ans1 = arr[m_index]
            ans2 = sum(x == arr[m_index] for x in arr)
            # 可能的M數量
            ans3 = 1 # 只有一個M
        else:  # 偶數
            # 最小的中位數
            m_index = len(arr) // 2 - 1
            ans1 = arr[m_index]
            # 數範圍兩個中位數之間的數字
            left = arr[m_index]
            right = arr[m_index + 1]
            ans2 = sum(left <= x <= right for x in arr)
            # 可能的M數量
            ans3 = right - left + 1

        # 輸出
        print(f'{ans1} {ans2} {ans3}')

    except EOFError:
        break