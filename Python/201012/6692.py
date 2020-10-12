# 다솔이의 월급 상자

test = int(input())

for case in range(test):
    num = int(input())
    avg  = 0
    for i in range(num):
        percentage, money = map(float, input().split())
        avg += money * percentage
    avg = '%0.6f' % avg
    print(f'#{case + 1} {avg}')