# 파리 퇴치

test = int(input())

for case in range(test):
    sum = 0
    die = 0
    N, M = map(int, input().split())
    arr = [[0 for column in range(N)] for row in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += arr[i+k][j+l]
                
            if sum > die: die = sum
    print(f'#{case+1} {die}')
       
    # for i in range(N-M+1):
    #     # arr[i][j]~arr[i][j+N-1]
    #     # .
    #     # .
    #     # .       
    #     # arr[i+N-1]~arr[i+N-1] 의 합
    #     for j in range(N-M+1):
    #         arr[i][j]
    