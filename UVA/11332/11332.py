def cal(line):
    if int(line) < 10:
        return line
    else:
        line_arr = list(line)
        new_num = 0
        for e in line_arr:
            new_num += int(e)
        return cal(str(new_num))


while True:
    try:
        line = input()
        if line == '0':
            break
        print(cal(line))
    except EOFError: # Domjudge測資問題迴避
        break