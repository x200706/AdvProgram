while True:
    a, b = map(int, input().split())
    print(f'{a} {b}')
    if a == 0 and b == 0:
        break
    arr = []
    for i in range(a):
        arr.append(int(input()))
    def mod(a, b):
        result = abs(a) % abs(b)
        if a < 0:
            result *= -1
        return result
    def sort_key(x):
        return (mod(x, b), x % 2 == 0, -x if x % 2 != 0 else x)
    ans = sorted(arr, key=sort_key)
    for e in ans:
        print(e)
# FYI: https://blog.iddle.dev/public/2024/04/27/Python-UVa-11321-Sort-Sort-and-Sort/