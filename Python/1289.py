# 원재의 메모리 복구하기

test = int(input())
for case in range(test):
    n = input()
    s = '0' * len(n)
    cnt = 0
    for i in range(len(n)):
        if i==0:
            if n[i]!=s[i]:
                s = n[i]*len(n)
                cnt += 1
        else:
            if n[i]!=s[i]:
                s = s[:i]
                new = n[i]*(len(n)-i)
                s += new
                cnt += 1
    print(f'#{case+1} {cnt}')