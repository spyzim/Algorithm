# 회문1

for test in range(10):
    N = int(input())
    arr = [input() for i in range(8)]   
    count = 0
    for i in range(8):
        temp = ''
        for j in range(8):
            temp += arr[j][i]
        for r in range(8-N+1):
            if arr[i][r:r+N] == arr[i][r:r+N][::-1]:
                count += 1
            if temp[r:r+N] == temp[r:r+N][::-1]:
                count += 1
 
    print(f'#{test+1} {count}')