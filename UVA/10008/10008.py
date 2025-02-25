# 解題思路：正則表達式留下英文 然後全轉大寫登記進table 算次數
import re

table = {}

while True:
    try:
        line = input()
        line_after_regex = re.sub('[^a-zA-Z]', '', line)
        line_list = list(line_after_regex.upper())
        print(line_list)
        #sort dict
    except EOFError:
        break