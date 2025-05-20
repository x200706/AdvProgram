while True:
    try:
        cur, tar = map(int, input().split())
        if cur == -1 and tar == -1:
            break
        print(min(abs(cur-tar),100-abs(cur-tar)))
    except EOFError:
        break