# 중간 평균값 구하기

test = int(input())

for case in range(test):
    nums = list(map(int, input().split()))
    nums.sort()
    del nums[0]
    del nums[8]

    avg = sum(nums) // len(nums)
    print(f'#{case + 1} {avg}')