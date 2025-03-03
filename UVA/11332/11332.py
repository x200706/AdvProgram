def super_sum(n): # 2
    if int(n) < 10:
        return n
    elif int(n) >= 10:
        n_digi_arr = list(n)
        n_digi_arr_to_int = (int(x) for x in n_digi_arr)
        n_digi_sum = sum(n_digi_arr_to_int)
        return super_sum(str(n_digi_sum))


while True:
    line = input().strip()
    if not line:
        continue
    if line == '0':
        break
    print(super_sum(line))