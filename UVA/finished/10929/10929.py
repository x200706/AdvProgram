while True:
    line = input()
    if line == '0':
        break
    if int(line) % 11 == 0:
        print(f'{line} is a multiple of 11.') # 小心這題測資有開頭為0的 要保留原樣輸出啊!!
    else:
        print(f'{line} is not a multiple of 11.')   