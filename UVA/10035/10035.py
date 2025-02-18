# CPE 10035 https://zerojudge.tw/ShowProblem?problemid=c014
# 123 456
# 555 555
# 123 594
# 0 0
# python 10035.py < 1.in > 1.out
while True:
  line = input()
  line_list = line.split() # domjudge空格問題
  num = int(line_list[0])
  next_num = int(line_list[1])

  if num == 0 and next_num == 0: # stdin真的要注意型別欸==
    break

  carry = 0
  carry_count = 0
  while num > 0 or next_num > 0:
    if num % 10 + next_num % 10 + carry >= 10:
      carry_count += 1
      carry = 1
      num = num // 10
      next_num = next_num // 10
    else:
      carry = 0
      num = num // 10
      next_num = next_num // 10

  if carry_count == 1:
    print('1 carry operation.') # Python預設就會換行了
  elif carry_count == 0:
    print('No carry operation.')
  else:
    print(str(carry_count) + ' carry operations.')
    

# No carry operation.
# 3 carry operations.
# 1 carry operation.