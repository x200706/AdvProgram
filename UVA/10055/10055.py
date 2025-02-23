# CPE 10055 https://zerojudge.tw/ShowProblem?problemid=a012
# 10 12
# 14 10

# 處理到EOF
while True: # 外面要有一個迴圈才能用break
  try:
    line = input()
    line = line.split(' ') # 每題測資空格不一樣？這題為什麼這樣寫系統就給過
    print(abs(int(line[0]) - int(line[1])))
  except EOFError:
    break

# 2
# 4