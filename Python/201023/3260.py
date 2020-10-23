# 두 수의 덧셈

test = int(input())

for case in range(test):
    A, B = map(int, input().split())
    print(f'#{case+1} {A+B}')