def get_part_one(ccc):
    s = len(ccc)-1
    ans = 0
    for c in ccc:
        index = ord(c)-ord('A')
        ans += index * 26**s
        s-=1
    return ans
        

cases = int(input())
for _ in range(cases):
    ccc, nums = input().split('-')
    ccc = get_part_one(ccc)
    if abs(ccc-int(nums)) <= 100:
        print('nice')
    else:
        print('not nice')