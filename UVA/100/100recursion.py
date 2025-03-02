table = {}
def cal(n):
    n_deal = n
    if n in table.keys():
        return table[n]
    elif n == 1:
        return 1
    elif n % 2 == 0:
        n_deal = n // 2
    else:
        n_deal = 3 * n + 1
    table[n] = cal(n_deal) + 1
    return table[n]

while True:
    try:
        a, b = map(int, input().split())
        o_a, o_b = a, b
        if a > b:
            a, b = b, a
        max_count = 0   
        for i in range(a, b + 1):
            num_count = cal(i)
            if num_count > max_count:
                max_count = num_count
        print(f'{o_a} {o_b} {max_count}')
    except EOFError:
        break
# 也能看看https://github.com/jlhung/UVA-Python/blob/master/100%20-%20The%203n%20%2B%201%20problem.py