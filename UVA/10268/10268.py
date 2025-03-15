while True:
    try:
        x = int(input())
        nums = list(map(int, input().split()))
        ans = 0
        n = len(nums) - 1
        for i in range(n, 0, -1):
            ans = ans * x + i * nums[n - i]
        print(ans)
    except EOFError:
        break