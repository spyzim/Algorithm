# 새로운 불면증 치료법

test = int(input())

for case in range(test):
    n = int(input())
    lst = []
    new_lst = []
    mul = 1    
    while True:
        room = n * mul
#        lst.append([int(i) for i in str(n)])  # room의 각 숫자를 lst 리스트의 요소로 넣는다(추가한다) -> 2차원 리스트가 된다.
        lst += [str(i) for i in str(room)]          # room의 각 숫자를 lst 리스트의 요소로 합친다.
       
        for v in lst:                     # 중복되는 숫자를 가진 요소를 제거    
            if v not in new_lst:
                new_lst.append(v)
        #new_lst.sort()                        # 오름차순 정렬 /굳이 필요 없다.
        if len(new_lst) == 10:              # 0~9 총 10개의 요소를 충족했을 경우, 탈출
            break
        mul += 1
    print(f'#{case + 1} {room}')
