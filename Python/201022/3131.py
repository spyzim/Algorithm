# 100만 이하의 모든 소수

# for i in range(1, 1000001):
#     divisor = []
#     for j in range(1, i+1):
#         if i % j == 0:
#             divisor.append(j)
#     if len(divisor) == 2:
#         print(i, end=" ")

def prime(n):
    a = [False, False] + [True] * (n - 1) 
    for k in range(2, int(n ** 0.5 + 1.5)):
        if a[k]: 
            a[k*2::k] = [False] * ((n - k) // k) 
    return [x for x in range(n+1) if a[x]]
print(' '.join(map(str, prime(10**6))))
