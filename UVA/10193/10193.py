def gcd(a, b): 
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b) 

I = int(input())
for _ in range(I):
    # 二進位要先轉十進位
    a = int(input(), 2)
    b = int(input(), 2)
    if gcd(a, b) != 1:
        print(f'Pair #{_+1}: All you need is love!')
    else:
        print(f'Pair #{_+1}: Love is not all you need!')