# 중간값 찾기

a = int(input())
nums = list(map(int,input().split()))
nums.sort()

print(nums[a//2])