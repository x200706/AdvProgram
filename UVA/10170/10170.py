import math

while True:
    try:
        day_one_guest, day = map(int, input().split())
        ans = int(math.ceil((-1 + ((1 - 4 * (-(day_one_guest ** 2) + day_one_guest - 2 * day))) ** 0.5) / 2))
        print(ans)
    except EOFError:
        break