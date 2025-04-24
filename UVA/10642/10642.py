case = int(input())

def get_number(x, y):
    return ((x + y) * (x + y + 1)) // 2 + x - 1

for _ in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    ans = get_number(x2, y2) - get_number(x1, y1)
    print(f'Case {_ + 1}: {ans}')