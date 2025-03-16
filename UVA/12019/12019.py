months_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

num = int(input())

for _ in range(num):
    m, d = map(int, input().split())
    days = d
    for i in range(m - 1):
        days += months_day[i]
    print(week_day[(days - 1) % 7])