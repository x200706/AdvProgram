import sys
from collections import Counter

def solve(trees):
    count = Counter(trees)
    n = len(trees)
    for k in sorted(count):
        percentage = round(count[k] * 100.0 / n, 4)
        print(f"{k} {percentage:.4f}")

T = int(input())
for t in range(T):
    trees = []
    if t == 0: input() # 第一個測資會有空行
    if t != 0: print() # 每個測資之間要空行
    while True:
        try:
            tree = sys.stdin.readline().strip()
            if tree:
                trees.append(tree)
            else:
                solve(trees)
                break
        except EOFError:
            solve(trees)
            break
# 參考：https://blog.iddle.dev/public/2023/05/23/Python-UVa-10226-Hardwood-Species/
# 這題真的很難過