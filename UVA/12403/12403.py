case = int(input())
total = 0
for _ in range(case):
    line_arr = input().split()
    command = line_arr[0]
    if command == 'donate':
        total+=int(line_arr[1])
    else:
        print(total)