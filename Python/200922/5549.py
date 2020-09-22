# 홀수일까 짝수일까

test = int(input())

for case in range(test):
    num = list(input())
    judge = num[-1:]
    if int(judge[0]) % 2 == 0:
        print(f'#{case + 1} Even')
    else:
        print(f'#{case + 1} Odd')