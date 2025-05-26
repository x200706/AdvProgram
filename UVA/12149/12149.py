while True:
    try:
        bound = int(input())
        if bound == 0:
            break
        ans = 0
        for i in range(1, bound+1):
            ans+= i**2
        print(ans)
    except EOFError:
        break