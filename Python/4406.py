# 모음이 보이지 않는 사람

test = int(input())
 
for case in range(test):
    data = input()
    collection = ['a', 'e', 'i', 'o', 'u']
 
    answer = ''
    for i in data:
        if i not in collection:
            answer += i
    print(f'#{case} {answer}')

        