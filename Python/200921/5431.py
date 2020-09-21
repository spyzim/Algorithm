# 민석이의 과제 체크하기

test = int(input())

for case in range(test):
    students_num, submit = map(int, input().split())
    submit_students = list(map(int, input().split()))
    students_all = []
    for i in range(1, students_num + 1):
        students_all.append(i)
    for i in submit_students:
        students_all.remove(i)
    print(f'#{case+1}', end = " ")
    for i in students_all:
        print(i, end = " ")
    print()
    