#TODO 來研究遞迴版本
table = {}

def cal(n):
    if n in table:
        return table[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        cycle_length = 1 + cal(n // 2)
    else:
        cycle_length = 1 + cal(3 * n + 1)
    table[n] = cycle_length
    return cycle_length

while True:
    try:
        line = input().strip()
        if not line:
            continue
        a, b = map(int, line.split())
        original_a, original_b = a, b
        if a > b:
            a, b = b, a
        max_time = 0
        for i in range(a, b + 1):
            current_time = cal(i)
            if current_time > max_time:
                max_time = current_time
        print(f'{original_a} {original_b} {max_time}')
    except EOFError:
        break