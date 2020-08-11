# 가랏! RC카!

test = int(input())

for case in range(test):
    command_num= int(input())
    distance = 0
    accel = 0
    move = 0
    for command in range(command_num):
        # a, s = map(int, input().split())        #a == 0 일 때의 경우 이러한 입력이 되지 않는다.
        a = list(map(int, input().split()))
        if a[0] != 0:
            accel = a[1]
            if a[0] == 1:
                move = move + accel
            else:
                move = move - accel
                if move < 0:
                    move == 0
        distance = distance + move
    print(f'#{case + 1} {distance}')
