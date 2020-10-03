# 최대수 구하기

test = int(input())

for i in range(test):
    nums = list(map(int, input().split()))
    nums.sort(reverse = True)
    print(f'#{i+1} {nums[0]}')

# nums[::-1]  뒤집기에 자주 사용
