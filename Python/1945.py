# # 간단한 소인수분해

nums=[2,3,5,7,11]

for a in range(int(input())) :
    n=int(input())
    print(f'#{a+1} ',end ='')
    for i in nums:
        log=0
        while True:
            if n%i or n <= 1:
                break
            n = n//i
            log+=1
        print(log,end=' ')
    print()
