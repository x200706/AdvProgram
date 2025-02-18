while True:
    try:
        input_num = input()
        print(input_num + ' is the input number')
    except EOFError:
        break