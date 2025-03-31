def division(a, b):
    arr = [a]
    current = a
    while current > 1:
        if current % b != 0:  
            return arr, False
        current //= b
        arr.append(current)
    return arr, (current == 1)

while True:
    try:
        a, b = map(int, input().split())
        if a <= 1 or b <= 1 or b == 0:
            print("Boring!")
            continue
        check_arr, valid = division(a, b)
        if valid:
            print(*check_arr)
        else:
            print("Boring!")
    except EOFError:
        break