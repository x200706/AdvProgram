while True:
    try:
        bottle = int(input())
        print(f'{int(bottle * 1.5)}')
    except EOFError:
        break