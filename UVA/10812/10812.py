n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    flag = True
    if (num1 % 2 != 0) or (num1 < num2):
        flag = False
    a = (num1 + num2) / 2
    b = a - num2
    if b < 0 or flag is False:
        print('impossible')
    else:
        print(f'{int(a)} {int(b)}')