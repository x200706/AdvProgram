months_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

num = int(input())

for _ in range(num):
    mon, day = map(int, input().split())
    day_from_start = day
    for i in range(mon - 1):
        day_from_start += months_day[i]
    print(week_day[(day_from_start - 1) % 7])