num = int(input())
for I in range(num):
    a = int(input())
    b = int(input())
    ans = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            ans += i
    print(f'Case {I + 1}: {ans}')