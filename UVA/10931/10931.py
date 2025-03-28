#TODO 轉二進位然後告訴有幾個1
def num_to_binary_and_rtn_1(n):
    binary = []
    while True: # FYI https://ithelp.ithome.com.tw/articles/10231314
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

while True:
    try:
        line = int(input())
        if not line:
            continue
        binary, one_num = num_to_binary_and_rtn_1(line)
        print(f'The parity of {''.join(binary)} is {one_num} (mod2).')
    except EOFError:
        break