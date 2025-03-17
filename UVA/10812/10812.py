n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    flag = True

    # 提前終止
    if num2 > num1 or ((num1 + num2) % 2 != 0):
        print('impossible')
        continue

    a = (num1 + num2) / 2
    b = a - num2
    if b < 0:
        print('impossible')
    else:
        print(f'{int(a)} {int(b)}')