# CPE 10041 https://zerojudge.tw/ShowProblem?problemid=a737
# 3
# 2 2 4
# 3 2 4 6
# 4 2 1 999 5
# python 10041.py < 1.in > 1.out
num = int(input())
for _ in range(num):
    line = list(map(int, input().split()))
    mid_index = line[0] // 2
    ne_list = line[1:]
    ne_list.sort() # 測試資料有可能鄰居是亂序的= =
    mid = ne_list[mid_index]     
    ans = sum(abs(x - mid) for x in ne_list)
    print(ans)

# 2 
# 4
# 1001