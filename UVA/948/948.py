#TODO 費波納契那題
I = int(input())

def get_fib():
    arr = [0, 1]  # F(0)=0, F(1)=1
    for i in range(2, 41):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr

fib = get_fib()[2:]  # 提前生成 Fibonacci 數列並去掉 0 和 1，只需生成一次

for _ in range(I):
    num = int(input())
    num_for_deal = num
    ans = ''
    
    # 從後往前遍歷（從大到小）
    for i in range(len(fib) - 1, -1, -1):
        if num_for_deal >= fib[i]:
            num_for_deal -= fib[i]
            ans += '1'
        elif ans:  # 只有在已經有 '1' 時才加 '0'，避免多餘的前導零
            ans += '0'
    
    # 如果 ans 為空，代表 num 是 0，直接輸出 0
    ans = ans or '0'
    print(f'{num} = {ans} (fib)')