#대각선 출력하기

arr = ['#', '+', '+', '+', '+']
 
for i in range(1,5):
    for j in range(5):
        print (arr[j], end='')
    arr[i] = '#'
    arr[i-1] = '+'
    print()
 
# 이 for문이 없는 더 깔끔한 코드가 있을까...
for i in range(5):
    print (arr[i], end='')