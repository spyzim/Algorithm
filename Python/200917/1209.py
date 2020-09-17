# Sum

for case in range(10):
    case_num = int(input())
    arr = [[0 for column in range(100)] for row in range(100)]
    for idx in range(100):
        arr[idx] = list(map(int, input().split()))

    max = 0
    # 각 열의 합
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum >= max:
            max = sum
    # 각 행의 합
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if sum >= max:
            max = sum
    #대각선의 합
    for i in range(100):
        sum = 0
        sum += arr[i][i]
        if sum >= max:
            max = sum
    for i in range(99, -1, -1):
        sum = 0
        sum += arr[i][i]
        if sum>= max:
            max = sum
    
    print(f'#{case_num} {max}')

        