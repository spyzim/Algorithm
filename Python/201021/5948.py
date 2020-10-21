# 새샘이의 7-3-5 게임

test = int(input())

for case in range(test):
    nums = list(map(int, input().split()))
    sum_list = []
    for i in range(7):
        for j in range(7):
            for k in range(7):
                if i == j or j == k or i == k:
                    continue
                if nums[i] + nums[j] + nums[k] not in sum_list:
                    sum_list.append(nums[i] + nums[j] + nums[k])
    sum_list.sort()
    print(f'#{case + 1} {sum_list[-5]}')