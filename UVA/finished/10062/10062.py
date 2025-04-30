while True:
    try:
        d = {}
        arr = list(input())
        for e in arr:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        sort_tuple = sorted(d.items(), key=lambda x: (x[1], -ord(x[0])))
        for k, v in sort_tuple:
            print(f'{ord(k)} {v}')
        print()
    except EOFError:
        break