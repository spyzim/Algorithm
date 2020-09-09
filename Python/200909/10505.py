# 소득 불균형

# 리스트의 평균을 구하는 함수
def avg(list, n):
    sum = 0
    for i in range(n):
        sum += list[i]
    average = sum // n
    return average

test = int(input())

for case in range(test):
    n = 0
    people = int(input())
    incomes = list(map(int, input().split()))
    for i in range(people):
        if incomes[i] <= avg(incomes, people):
            n += 1
    print(f'#{case + 1} {n}')