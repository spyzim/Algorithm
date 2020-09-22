# 최대 성적표 만들기

test = int(input())

for case in range(test):
    subject, select = map(int, input().split())
    scores = list(map(int, input().split()))
    max_scores = 0
    for i in range(select):
        max_scores += max(scores)
        scores.remove(max(scores))
    print(f'#{case + 1} {max_scores}')