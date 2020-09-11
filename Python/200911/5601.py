# 쥬스 나누기

test = int(input())

for case in range(test):
    people = int(input())
    print(f'#{case + 1}', end=" ")
    for juice in range(people):
        print(f'1/{people}', end=" ")
    print()
