#수도 요금 경쟁

test = int(input())

#(w*p)원이 크냐, q원 또는 (q + (w*s)) 원 이 크냐. 사용량은 (w) 리터이다, R 리터 이하**
for case in range(test):
    P, Q, R, S, W = map(int, input().split())
    bill = 0
    
    if W <= R :      # 사용량 w 가 r리터 이하인 경우.
        if (W*P) < (Q):
            bill = (W * P)
        else:
            bill = Q
    else:           #  사용량  w 가 r리터 초과인 경우.
        if (W*P) < (Q + ((W-R)*S)):
            bill = (W*P)
        else:
            bill = (Q + ((W-R)*S))
    
    print(f'#{case + 1} {bill}')



        
    
    

