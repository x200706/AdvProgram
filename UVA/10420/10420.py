table = {}

num = int(input())
for _ in range(num):
    line = input().split()
    if line[0] in table.keys():
        table[line[0]] += 1
    else:
        table[line[0]] = 1

for k, v in sorted(table.items(), key = lambda x : x[0]): # 這題要照國家字母排序
    print(f'{k} {v}')