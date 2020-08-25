# 간단한 압축 풀기

test = int(input())

for case in range(test):
    N = int(input())
    document = ''
    for i in range(N):
        Ci, Ki = input().split()
        Ki = int(Ki)
        while True:
            if Ki <= 0:
                break
            document += Ci
            Ki -= 1
    print(f'#{case + 1}')
    count = 1
    for alp in document:
        print(alp, end='')
        if count % 10 == 0:
            print()
        count += 1
    print()
    