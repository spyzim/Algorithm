# 비밀번호

# 리스트에서 같은 요소값은 제거하는 함수
def decode(list):
    judge = True
    while judge:
        for i in range(len(list) - 1 ):
            if list[i] == list[i+1]:
                del list[i:i+2]
                break
            elif i == len(list) - 2:
                judge = False
    return list
                
for case in range(10):
    length, password = input().split()
    password_arr = []
    for idx in password:
        password_arr.append(idx)

    print(f'#{case+1}', end=" ")
    for i in range(len(decode(password_arr))):
        print(decode(password_arr)[i], end="")
    print()
