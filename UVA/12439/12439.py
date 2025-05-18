# 這題是在問測資之間有幾個2/29
month_num = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

cases = int(input())
for case in range(cases):
    a = input().split()
    am = month_num[a[0]]
    ad = int(a[1].replace(',',''))
    ay = int(a[2])

    b = input().split()
    bm = month_num[b[0]]
    bd = int(b[1].replace(',',''))
    by = int(b[2])

    # 計算by之前有多少個閏年
    y_before_by = by - 1
    leap_day_count_for_b = (y_before_by // 4) - (y_before_by // 100) + (y_before_by // 400)
    
    if is_leap(by):
        if bm > 2:  # 如果是3月或之後，by的2月29日已過
            leap_day_count_for_b += 1
        elif bm == 2 and bd == 29: # 如果剛好是by的2月29日
            leap_day_count_for_b += 1

    # 計算ay之前有多少個閏年
    y_before_ay = ay - 1
    leap_day_count_for_a = (y_before_ay // 4) - (y_before_ay // 100) + (y_before_ay // 400)

    if is_leap(ay):
        # 如果是3月或之後，代表ay年的2月29日已經過去了；
        # 即便am ad是2月29日，這個2月29日也不算在"嚴格之前"
        if am > 2:
            leap_day_count_for_a += 1 # 為了對齊
            
    leap_day_count = leap_day_count_for_b - leap_day_count_for_a
    
    print(f'Case {case+1}: {leap_day_count}')
