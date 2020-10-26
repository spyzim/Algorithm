# 전봇대

test = int(input())

for case in range(test):
    lines = int(input())
    height_dict = {}
    count = 0
    for line in range(lines):
        Ai, Bi = map(int, input().split())
        height_dict[Ai] = Bi
    height_list = sorted(height_dict.items())

    for i in range(len(height_list)-1):
        for j in range(i+1, len(height_list)):
            if height_list[i][1] > height_list[j][1]:
                count += 1
    print(f'#{case + 1} {count}')


