# 直接算好像也不會timeout...？ https://github.com/jlhung/UVA-Python/blob/master/11461%20-%20Square%20Numbers.py
# 不一定要dp https://github.com/rezwanh001/UVA-Solutions-in-Python/blob/master/11461%20-%20Square%20Numbers.py
import math
while True:
    line = input()
    if line == '0 0':
        break
    a, b = map(int, line.split())
    
    start = math.ceil(a ** 0.5) #HINT 這邊得向上取整
    count = 0
    while True:
        new_num = start * start
        if new_num > b:
            break
        count += 1
        start += 1
    print(count)
# 取平方根相關：https://www.php.cn/zh-tw/faq/572702.html