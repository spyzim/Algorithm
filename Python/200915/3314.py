# 보충학습과 평균

# 보충 학습 후 점수
def arrange(n):
    if n < 40:
        return 40
    else:
        return n

test = int(input())

for case in range(test):
    a, b, c, d, e = map(int, input().split())
    sum = arrange(a) + arrange(b) + arrange(c) + arrange(d) + arrange(e)
    average = sum // 5
    print(f'#{case + 1} {average}')

