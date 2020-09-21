# USB 꽂기의 미스터리

# 올바른 면으로 꽂을 확률: p
# 올바른 면으로 꽂았을 때, 잘 들어갈 확률: q
# i 번 뒤집어 꽂힐 확률 si
# s1 은 (1-p)*q
# s2 은 p*(1-q)*q

test = int(input())

for case in range(test):
    p, q = map(float, input().split())
    s1 = (1-p) * q
    s2 = p * (1-q) * q
    if s1 < s2:
        print(f'#{case+1} YES')
    else:
        print(f'#{case+1} NO')