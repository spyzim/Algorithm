# 쉬운 거스름돈

test = int(input())

for case in range(test):
    N = int(input())
    changes = [0, 0, 0, 0, 0, 0, 0, 0]
    money = 50000
    for i in range(8):
        if N / money > 0:
            changes[i] = N // money
            N = N % money
        else:
            changes[i] = 0
        if i % 2 == 0:
            money = money // 5
        else:
            money = money // 2

    print(f'#{case + 1}')
    for index in range(len(changes)):
        print(changes[index], end=" ")
    print("")