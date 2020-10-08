# 두 가지 빵의 딜레마

test = int(input())

for case in range(test):
    bread_A, bread_B, money = map(int, input().split())
    cheaper = 0
    if bread_A > bread_B:
        cheaper = bread_B
    else:
        cheaper = bread_A
    maximum = money // cheaper
    print(f'#{case + 1} {maximum}')