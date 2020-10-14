# 큰 놈, 작은 놈, 같은 놈

test = int(input())
Ineql = [' ', ' ', ' ']

for i in range(test):
    a, b = map(int, input().split())
    if a > b:
        Ineql[i] = '>'
    elif a == b:
        Ineql[i] = '='
    else:
        Ineql[i] = '<'
    print(f'#{i+1} {Ineql[i]}')
