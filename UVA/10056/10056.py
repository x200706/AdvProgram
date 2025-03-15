num = int(input())
for _ in range(num):
    n, p, player = map(float, input().split())
    if p == 0:
        print(f'{0:.4f}')
    else:
        q = (1 - p)
        print(f'{p * (q ** (player - 1) / (1 - q ** n)):.4f}')