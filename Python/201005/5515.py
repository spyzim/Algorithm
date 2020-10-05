# 2016년 요일 맞추기

test = int(input())

for case in range(test):
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = [4, 5, 6, 0, 1, 2, 3]
    month, day = map(int, input().split())
    sum_of_day = day
    for i in range(month):
        sum_of_day += months[i]
    print(f'#{case+1} {days[(sum_of_day % 7) -1]}')     
