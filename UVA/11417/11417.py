def gcd(a, b): 
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b) 

while True:
    try:
        line = input()
        g = 0
        if line == '0':
            break

        for i in range(1, int(line)):
            for j in range(i + 1, int(line) + 1):
                g += gcd(i, j)
        
        print(g)
    except EOFError:
        break