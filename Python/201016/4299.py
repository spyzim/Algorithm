# 태혁이의 사랑은 타이밍

test =int(input())

for case in range(test):
    day, hour, minute = map(int, input().split())

    wait = 0
    
    if day > 11:
        wait = (1440 * (day - 11)) + (60 * (hour - 11)) + (minute - 11) 
    elif day == 11:
        if hour > 11:
            wait = (60 * (hour - 11)) + (minute - 11) 
        elif hour == 11:
            if minute > 11:
                wait = minute - 11
            elif minute == 11:
                wait = 0
            else:
                wait = -1
        else:
            wait = -1
    else:
        wait = -1

    print(f'#{case + 1} {wait}')

# 1분 = 1분
# 1시간 = 60분
# 1일 = 1440분