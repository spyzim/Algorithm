# 직사각혀 길이 찾기

test = int(input())

for case in range(test):
    a, b, c = map(int, input().split())
    print(f'#{case + 1}', end = " ")
    if a==b:
        print(c)
    elif a==c:
        print(b)
    else:
        print(a)
        