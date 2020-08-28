# 거듭 제곱

def power(N, M):    
    if M ==1:
        return N
    M -= 1
    return N * power(N,M)

for i in range(10):
    test_num = int(input())
    N, M = map(int, input().split())

    print(f'#{test_num} {power(N, M)}')