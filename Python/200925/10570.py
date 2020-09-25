# 제곱 팰린드롬 수

import math

# 인자로 받은 정수형 num 이 팰린드롬 수 인가 판별
def palindrom(num):
    num = str(num)
    num_reverse = num[::-1]
    if num == num_reverse:
        return True
    else:
        return False
    

test = int(input())

for case in range(test):
    num_start, num_end = map(int, input().split())
    count = 0
    for num in range(num_start, num_end + 1):
        square_num = float(math.sqrt(num))
        if (square_num * 10) % 10 == 0:
            square_num = int(square_num)
        if palindrom(num) == True and palindrom(square_num) == True:
            count += 1 
    
    print(f'#{case + 1} {count}')
