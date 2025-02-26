def solver(num):
    if num >= 10000000:
        solver(num // 10000000)
        print(' kuti', end='')
        num = num % 10000000
    if num >= 100000:
        solver(num // 100000)
        print(' lakh', end='')
        num = num % 100000
    if num >= 1000:
        solver(num // 1000)
        print(' hajar', end='')
        num = num % 1000
    if num >= 100:
        solver(num // 100)
        print(' shata', end='')
        num = num % 100
    if num >= 1:
        print(f' {num}', end='')

outline = 1
while True:
    try:
        # 還要印標號ㄟ
        num = int(input())
        print(f'{outline:>4}.', end='')
        if num == 0:
            print(' 0', end='')
        else:
            solver(num)
        outline += 1
        print('')
    except EOFError:
        break

