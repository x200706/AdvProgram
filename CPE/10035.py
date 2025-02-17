# CPE 10035 https://zerojudge.tw/ShowProblem?problemid=c014
# 123 456
# 555 555
# 123 594
# 0 0
while True:
  line = input()
  line_list = line.split(' ')
  num = int(line_list[0])
  next_num = int(line_list[1])

  if num == 0 and next_num == 0: # stdin真的要注意型別欸==
    break

  carry = 0
  while (num > 0 and next_num > 0):
    if num % 10 + next_num % 10 >= 10:
      carry += 1
      num = num // 10
      next_num = next_num // 10 + 1
    else:
      num = num // 10
      next_num = next_num // 10
  if carry == 1:
    print('1 carry operation.') # Python預設就會換行了
  elif carry == 0:
    print('No carry operation.')
  else:
    print(str(carry) + ' carry operations.')

# No carry operation.
# 3 carry operations.
# 1 carry operation.