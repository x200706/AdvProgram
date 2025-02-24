line_arr = list(map(int, input().split()))
line_arr.sort()
start = line[0]
end = line[1]
max_time = 0
table = {}
# 直到EOF
for i in range(start, end + 1):
    cal(i)
    
def cal(n):
    if n == 1:
        break
    # if n % 2 == 0:
    #      n // 2
    # else:
    #      3 * n + 1


print(f'{start} {end} {max_time}')
# 參考 https://github.com/jlhung/UVA-Python/blob/master/100%20-%20The%203n%20%2B%201%20problem.py
