def prime_list(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    
    primes = [num for num in range(max_num + 1) if is_prime[num]]
    return primes

primes = prime_list(1000000)

while True:
    try:
        line = input()
        reversed_line = ''.join(list(reversed(list(line))))
        if (int(line) not in primes):
            print(f'{line} is not prime.')
        elif (int(reversed_line) not in primes) or (int(line) == int(reversed_line)):
            print(f'{line} is prime.')
        elif (int(line) in primes) and (int(reversed_line) in primes):
            print(f'{line} is emirp.')
    except EOFError:
        break