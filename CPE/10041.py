# CPE 10041 https://zerojudge.tw/ShowProblem?problemid=a737
# 3
# 2 2 4
# 3 2 4 6
# 4 2 1 999 5

num = int(input()) 
cal_list = []
for i in range(0, num):
  test_group = input()
  cal_list.append(test_group.split(' '))

for e in cal_list:
  # 取中位數要分奇數偶數
  mid_index = 0
  if (int(e[0]) % 2 != 0):
    mid_index = int(e[0]) // 2
  else:
    mid_index = int(e[0]) // 2 - 1
  ne_list = e[1:]
  ne_list.sort()

  mid = int(ne_list[mid_index])

  line_ans = 0
  for sub_e in ne_list:
    temp_d = int(sub_e) - mid
    line_ans += abs(temp_d)
  print(line_ans)

# 2 
# 4
# 1001