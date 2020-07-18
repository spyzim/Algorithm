# 두 개의 숫자열

#     # lst_a[0] * lst_b[i]
#     # lst_a[1] * lst_b[i+1]
#     # lst_a[2] * lst_b[i+2]
#     # .
#     # .
#     # .
#     # lst_a[n-1] * lst_b[i+n-1]    -> n개의 요소를 가지고 있는 lst_a 와 임의의 lst_b 의 곱        
#     # i + n - 1 <= m - 1 and i >= 0
#     # i >= 0 and i <= m - n  

test = int(input())

for case in range(test):
    N, M = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    sm_len = 0
    lg_len = 0
    is_N_big = True
    max = 0
    if M > N:
        sm_len = N
        lg_len = M
        is_N_big = False
    else:
        sm_len = M
        lg_len = N
 
    for i in range(lg_len - sm_len + 1):
        sum = 0
        for j in range(sm_len):
            if is_N_big:
                sum += lst_b[j] * lst_a[i+j]
            else:
                sum += lst_a[j] * lst_b[i+j]
        if sum > max:
            max = sum
 
    print(f'#{case+1} {max}')