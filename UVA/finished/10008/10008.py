# 解題思路：正則表達式留下英文 然後全轉大寫登記進table計次數
import re

table = {}

while True:
    try:
        line = input()
        line_after_regex = re.sub('[^a-zA-Z]', '', line)
        line_list = list(line_after_regex.upper())
        for e in line_list:
            if e in table.keys():
                table[e] += 1
            else:
                table[e] = 1
    except EOFError:
        break

for k, v in sorted(table.items(), key = lambda x : (-x[1], x[0])):
    print(k, v)
# FYI https://gdst.dev/posts/UVA-10008/