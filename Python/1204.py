# 최빈수 구하기

test = int(input())

for case in range(test):
    test_case = int(input())
    scores = list(map(int, input().split()))
    count_dic = {}
    for score in scores:
        if score in count_dic:
            count_dic[score] += 1
        else:
            count_dic[score] = 1
    
    max = 0
    mode = 0
    for key, value in count_dic.items():
        if max < value:
            max = value
            mode = key
        elif max == value:
            if mode < key:
                mode = key
    
    print(f'#{case + 1} {mode}')