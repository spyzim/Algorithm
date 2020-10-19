# 수의 새로운 연산

# 1,1 = 1

# 1,2 = 2
# 2,1 = 3

# 1,3 = 4
# 2,2 = 5
# 3,1 = 6

# 1,4 = 7
# 2,3 = 8
# 3,2 = 9
# 4,1 = 10

# 1,5 = 11
# 2,4 = 12
# 3,3 = 13
# 4,2 = 14
# 5,1 = 15

# 1,6 = 16
# 2,5 = 17
# 3,4 = 18
# 4,3 = 19
# 5,2 = 20
# 6,1 = 21
# .
# .
# .

test = int(input())
N = 300
maps = [ [0 for _ in range(N+2) ] for _ in range(N+2)]
maps[1][1] = 1
cnt = 1
for y in range(1, N+1):
    maps[y + 1][1] = y + maps[y][1]
    cnt += 1
    k = cnt
    for x in range(2, N+1):
        maps[y][x] = maps[y][x-1] + k
        k += 1
for case in range(1, test+1):
    p, q = map(int, input().split())
    for y in range(1, N+1):
        for x in range(1, N+1):
            if maps[y][x] == p:
                px = x
                py = y
            if maps[y][x] == q:
                qx = x
                qy = y
    
    result_x = px + qx
    result_y = py + qy
    for y in range(1, N+1):
        for x in range(1, N+1):
            result = maps[result_y][result_x]

    print(f'#{case} {result}')
