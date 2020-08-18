# 시각 덧셈

test = int(input())

for case in range(test):
    time = list(map(int, input().split()))

    hour = time[0] + time[2]
    min = time[1] + time[3]

    if min > 59:
        hour = hour + 1
        min = min - 60
    
    if hour >12:
        hour = hour -12
    
    print(f'#{case+1} {hour} {min}')