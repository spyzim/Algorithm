# 농작물 수확하기

# 2차원 리스트를 받아, 마름모 모양의 요소값들의 합을 구하는 함수
def revenue(list):
    N = len(list[0])
    all = 0
    idx = 0
    for i in range((N//2) + 1):
        list_new = list[i][(N//2)-i:(N//2)+i+1]
        all += sum(list_new)

    for i in range(N - 1, (N//2), -1):
        list_new = list[i][(N//2)-idx:(N//2)+idx+1]
        idx += 1
        all += sum(list_new)

    return all    

test = int(input())

for case in range(test):
    N = int(input())
    arr = [[0 for column in range(N)] for row in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input()))
    if N == 1:
        print(f'#{case + 1} {arr[0][0]}')
    else:
        print(f'#{case + 1} {revenue(arr)}')

