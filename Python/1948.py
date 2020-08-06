# 날짜 계산기

test = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for case in range(test):
    early_m, early_d, late_m, late_d = map(int, input().split())
    diff = late_d - early_d + 1
    for month in range(early_m, late_m):
        diff += days[month - 1]
    print(f'#{case + 1} {diff}')