# 지그재그 숫자

test = int(input())

for i in range(0,test):
    sum = 0
    num = int(input())
    for j in range(1, num+1):
        if j % 2 != 0:
            sum += j
        else: 
            sum -= j

    print(f'#{i+1} {sum}')
