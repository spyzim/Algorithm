# 암호생서기

# 리스트를 받아 첫번째 요소에 n 을 뺀 후 맨 뒤로 이동시키는 함수. 
def coding(list1, n, judge):
    list1[0] -= n
    if list1[0] <= 0:
        list1[0] = 0
        judge = 0
    temp = list1[0]

    for i in range(7):
        list1[i] = list1[i+1]
    list1[7] = temp

for case in range(2):
    case_num = int(input())
    code = list(map(int, input().split()))
    judge = 1
    while True:
        for i in range(1,5):
            coding(code, i, judge)
            if judge == 0:
                break
    print(f'{case_num + 1}', end = " ")
    for i in range(8):
        print(code[i], end = " ")
    print()

