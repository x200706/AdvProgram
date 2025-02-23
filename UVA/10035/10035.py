# CPE 10035 https://zerojudge.tw/ShowProblem?problemid=c014
# 123 456
# 555 555
# 123 594
# 0 0
# python 10035.py < 1.in > 1.out
while True:
    line = input()
    if line == '0 0':
        break
    line_arr = list(map(int, line.split()))
    num = line_arr[0]
    next_num = line_arr[1]
    carry = 0
    carry_time = 0
    while num > 0 or next_num > 0:
        if num % 10 + next_num % 10 + carry >= 10:
            carry_time += 1
            carry = 1
        else:
            carry = 0
        num = num // 10
        next_num = next_num // 10

    if carry_time == 0:     
        print('No carry operation.')
    elif carry_time == 1:
        print('1 carry operation.')
    else:
        print(f'{carry_time} carry operations.')
    

# No carry operation.
# 3 carry operations.
# 1 carry operation.