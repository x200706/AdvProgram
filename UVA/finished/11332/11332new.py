def solve(input_str):
    if int(input_str) < 10:
        return input_str
    else:
        new_num = 0
        line_arr = list(input_str)
        for e in line_arr:
            new_num += int(e)
        return solve(str(new_num))

while True:
    try:
        line = input()
        if line == '0':
            break
        print(solve(line))
    except EOFError:
        break