# 숫자를 정렬하자

test = int(input())

for case in range(test):
    nums = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f'#{case + 1}', end=' ')
    num = 0
    for num in range(nums):
        print(arr[num], end=' ')
    print("")
