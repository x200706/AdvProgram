
def find_nine_mult(num_str):
    flag = False
    times = 1

    str_list = list(num_str)
    str_sum = sum(map(int, str_list))

    if str_sum == 9:
        return True, 1

    while (str_sum % 9 == 0):
        if str_sum == 9:
            break
        new_str = list(str(str_sum))
        str_sum = sum(map(int, new_str))
        flag = True
        times += 1

    return flag, times

while True:
    try:
        line = input()
        if line == '0':
            break
        ans, times = find_nine_mult(line)
        if ans == False:
            print(f'{line} is not a multiple of 9.')
        else:
            print(f'{line} is a multiple of 9 and has 9-degree {times}.')
    except EOFError:
        break
