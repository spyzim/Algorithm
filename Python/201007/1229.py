# 암호문 2

for test_case in range(10):
    code_length = int(input())
    code = list(map(int, input().split()))
    incoding_num = int(input())
    incoding = list(input().split())
    for i in range(len(incoding)):
        if incoding[i] == 'I':
            for j in range(int(incoding[i+2])):
                code.insert(j+int(incoding[i+1]), int(incoding[i+3+j]))
        if incoding[i] == 'D':
            for j in range(int(incoding[i+2])):
                del code[int(incoding[i+1])+j]

    list_new = code[:10]
    print(f'#{test_case+1}', end = ' ')
    for i in list_new:
        print(i, end = ' ')
    print()       