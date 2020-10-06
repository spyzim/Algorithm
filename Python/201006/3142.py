# 영준이와 신비한 뿔의 숲

test = int(input())

for case in range(test):
    horns, animals = map(int, input().split())
    # for i in range(1, animals + 1):
    #     single_horn = i
    #     twin_horns = animals - i
    #     if single_horn + (2 * (twin_horns)) == horns:
    #         break
    # print(f'#{case + 1} {single_horn} {twin_horns}')
    print(f'#{case + 1} {(2*animals) - horns} {horns - animals}')