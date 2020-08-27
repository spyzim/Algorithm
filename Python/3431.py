# 준환이의 운동관리

def judge(l, u, x):
    if x < l:
        print(l - x)
    elif x > u:
        print( -1 )
    else:
        print( 0 )

test = int(input())

for case in range(test):
    min, max, exercise = map(int, input().split())
    print(f'#{case + 1}', end = " ")
    judge(min,max,exercise)