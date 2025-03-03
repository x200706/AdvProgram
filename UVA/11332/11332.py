def super_sum(n): # 遞迴解
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

# 優秀題解
# https://github.com/rezwanh001/UVA-Solutions-in-Python/blob/master/11332_Summing_Digits.py while與字串處理
# https://blog.iddle.dev/public/2024/04/21/Python-UVa-11332-Summing-Digits/#google_vignette 數學解
# https://github.com/jlhung/UVA-Python/blob/master/11332%20-%20Summing%20Digits.py