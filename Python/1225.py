# 암호생서기

# 리스트를 받아 첫번째 요소에 n 을 뺀 후 맨 뒤로 이동시키는 함수. 
# def coding(list1, n, j):
#     list1[0] -= n
#     if list1[0] <= 0:
#         list1[0] =0
#         j -= j
#     temp = list1[0]

#     for i in range(7):
#         list1[i] = list1[i+1]
#     list1[7] = temp

for case in range(10):
    case_num = int(input())
    code = list(map(int, input().split()))
    judge = 1
    while True:
        for i in range(1,6):
            code[0] -= i
            if code[0] <= 0:
                code[0] = 0
            temp = code[0]

            for j in range(7):
                code[j] = code[j+1]
            code[7] = temp

            if code[7] == 0:
                break
        if code[7] == 0:
            break
    print(f'#{case_num}', end = " ")
    for i in range(8):
        print(code[i], end = " ")
    print()

