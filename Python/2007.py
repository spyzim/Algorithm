# 패턴 마디의 길이

test = int(input())

for case in range(test):
    pattern = input()
    num = 1
    while True:
        if pattern[0:num] == pattern[num:2*num]: break
        num += 1
    print(f'#{case+1} {num}')

