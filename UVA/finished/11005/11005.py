def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digit = n % base
        if digit < 10:
            digits.append(str(digit))
        else:
            digits.append(chr(ord('A') + digit - 10))
        n //= base
    return ''.join(digits[::-1])

def calc_cost(num_str, costs):
    total = 0
    for digit in num_str:
        if digit.isdigit():
            total += costs[int(digit)]
        else:
            total += costs[ord(digit) - ord('A') + 10] 
    return total

T = int(input())
for case in range(T):
    costs = []
    for _ in range(4):
        line = list(map(int, input().split()))
        costs.extend(line)
    
    Q = int(input())
    print(f"Case {case + 1}:")
    
    for _ in range(Q):
        num = int(input())
        base_costs = []
        for b in range(2, 37):
            num_str = to_base(num, b)
            cost = calc_cost(num_str, costs)
            base_costs.append(cost)
        
        min_cost = min(base_costs)
        cheapest_bases = [i + 2 for i, cost in enumerate(base_costs) if cost == min_cost]
        
        print(f"Cheapest base(s) for number {num}: {' '.join(map(str, cheapest_bases))}")
    print()