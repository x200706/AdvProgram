case = int(input())
for _ in range(case):
    a, b, c  = map(int, input().split())
    if a<=20 and b<=20 and c<=20:
        print(f'Case {_+1}: good')
    else:
        print(f'Case {_+1}: bad')