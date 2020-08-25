# 조교의 성적 매기기

test = int(input())

for case in range(test):
    students, student = map(int, input().split())
    totals = []
    T = 0
    for scores in range(students):
        mid, final, hw = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (hw * 0.2)
        totals.append(total)
        if scores + 1 == student:
            T = total

    totals.sort(reverse=True)
    T = totals.index(T) + 1
    print(f'#{case + 1}', end = " ")
    if T <= students // 10:
        print("A+")
    elif T <= 2 * (students // 10):
        print("A0")
    elif T <= 3 * (students // 10):
        print("A-")
    elif T <= 4 * (students // 10):
        print("B+")
    elif T <= 5 * (students // 10):
        print("B0")
    elif T <= 6 * (students // 10):
        print("B-")
    elif T <= 7 * (students // 10):
        print("C+")
    elif T <= 8 * (students // 10):
        print("C0")
    elif T <= 9 * (students // 10):
        print("C-")
    elif T <= students:
        print("D0")
    
