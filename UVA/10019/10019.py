#TODO 第一個十進位數字轉成二進位告訴有幾個1；第二個是十六進位數字 做一樣的事情
# 先做10931再做這題

def num_to_binary_and_rtn_1(n):
    binary = []
    while True: 
        digi = n // 2
        binary_digi = n % 2
        binary.insert(0, str(binary_digi))
        n = digi
        if n == 0:
            break
    one = 0
    for digi in list(binary):
        if digi == '1':
            one += 1
    return binary, one
def hex_to_binary_and_rtn_1(n):
    ten_num = int(str(n), 16)
    b, a = num_to_binary_and_rtn_1(ten_num)
    one = 0
    for digi in b:
        if digi == '1':
            one += 1
    return one

I = int(input())
for _ in range(I):
    line = int(input())

    binary, binary_one_num = num_to_binary_and_rtn_1(line)
    hex_one_num = hex_to_binary_and_rtn_1(line)

    print(f'{binary_one_num} {hex_one_num}')
# Python內置函數版可參考 https://blog.iddle.dev/public/2023/03/20/Python-UVa-10019-Funny-Encryption-Method/