# Magnetic

for case in range(10):
    n = int(input())
    table = [[0 for column in range(n)] for row in range(n)]
    for i in range(n):
        table[i] = list(map(int, input().split()))
    # 1 은 아래로, 2 는 위쪽으로 이동.
    # table[0][0],table[1][0],table[2][0]....table[n-1][0] 을 비교해 교착상태를 판별한다.
    count = 0

    for i in range(n):
        check = 0
        for j in range(n):
            if table[j][i] == 0:
                continue
            elif check == 0 and table[j][i] == 2:
                continue
            elif check == 1 and table[j][i] == 2:
                count += 1
                check = 0
            elif table[j][i] == 1:
                check = 1
    
    print(f'#{case + 1} {count}')
                

