# 달팽이 숫자

test = int(input())

for case in range(test):
    N = int(input())
    num = N
    arr = [[0 for column in range(N)] for row in range(N)]
    turn = 1
    x = 0
    y = -1
    index = 1

    while(True):
        
        for i in range(N):
            y += turn
            arr[x][y] = index
            index += 1
        
        N -= 1
        
        for i in range(N):
            x += turn
            arr[x][y] = index
            index += 1
        
        turn *= -1
        
        if N == 0:
            break

    print(f'#{case + 1}')
    for i in range(num):
        for j in range(num):
            print(arr[i][j], end=" ")
        print()
