# 건초더미

test = int(input())

for case in range(test):
    nums = int(input())
    hay = []
    
    for num in range(nums):
        size = int(input())
        hay.append(size)
    avg = sum(hay)//nums
    move = 0

    for i in hay:
        if i < avg:
            move += avg - i
    
    print(f'#{case + 1} {move}')