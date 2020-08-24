# 파스칼의 삼각형

test = int(input())

for case in range(test):
    num = int(input())
    pascal = [[0 for col in range(num)] for row in range(num)]
    pascal[0][0] = 1
    for i in range(num):
        for j in range(i+1):
            if i == j:
                pascal[i][j] = 1
            elif j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

    print(f'#{case + 1}')

    for i in range(num):
        for j in range(i+1):
            print(pascal[i][j], end = " ")
            
        print(" ")