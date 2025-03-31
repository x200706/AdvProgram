# 讀取測試案例數量
T = int(input())

for _ in range(T):
    # 讀取總天數N
    N = int(input())
    # 讀取政黨數P
    P = int(input())

    # 讀取每個政黨的罷工週期
    h = []
    for i in range(P):
        h.append(int(input()))
    
    days = [False] * (N + 1)
    
    # 我這是窮舉，如果有兩個正如果有兩個政黨分別是隔2天跟4天罷工 那算2天就涵蓋了<-題目認為只要一天有一個黨罷工就算浪費了
    for hi in h:
        # 生成所有罷工天數
        for j in range(hi, N + 1, hi):
            if j % 7 != 6 and j % 7 != 0: # 非週末
                days[j] = True
    
    hartal_days = sum(days)
    print(hartal_days)