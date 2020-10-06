# 구독자 전쟁

test = int(input())

for case in range(test):
    people = list(map(int, input().split()))
    maximum = min(people)
    minimum = 0
    if people[0] < people[1] + people[2]:
        minimum = people[1] + people[2] - people[0]
    elif people[0] == people[1] and people[0] == people[2]:
        maximum = people[0]
        minimum = people[0]
    print(f'#{case + 1} {maximum} {minimum}')