# # 상호의 배틀필드

# test = int(input())

# for case in range(test):
#     height, width = map(int, input().split())
#     field = [[0 for column in range(width)] for row in range(height)]
#     for i in range(height):
#         field[i] = list(input())
#         if '<' in field[i]:
#             first_index = i
#             sec_index = field[i].index('<')
#         elif '>' in field[i]:
#             first_index = i
#             sec_index = field[i].index('>')
#         elif '^' in field[i]:
#             first_index = i
#             sec_index = field[i].index('^')
#         elif 'v' in field[i]:
#             first_index = i
#             sec_index = field[i].index('v')

#     command_num = int(input())
#     commands = input()

#     for command in commands:
#         if command == 'U':
#             try:
#                 if field[first_index-1][sec_index] == '.':
#                     field[first_index][sec_index] == '.'
#                     first_index = first_index - 1
#                     field[first_index][sec_index] == '^'
#                 elif field[first_index-1][sec_index] == '*' or field[first_index-1][sec_index] == '#' or field[first_index-1][sec_index] == '-':
#                     continue
#             except IndexError:
#                 continue
                
#         elif command == 'D':
#             try:
#                 if field[first_index+1][sec_index] == '.':
#                     field[first_index][sec_index] == '.'
#                     first_index = first_index + 1
#                     field[first_index][sec_index] == 'v'
#                 elif field[first_index+1][sec_index] == '*' or field[first_index+1][sec_index] == '#' or field[first_index+1][sec_index] == '-':
#                     continue
#             except IndexError:
#                 continue

#         elif command == 'L':
#             try:
#                 if field[first_index][sec_index-1] == '.':
#                     field[first_index][sec_index] == '.'
#                     sec_index = sec_index - 1
#                     field[first_index][sec_index] == '<'
#                 elif field[first_index][sec_index-1] == '*' or field[first_index][sec_index-1] == '#' or field[first_index][sec_index-1] == '-':
#                     continue
#             except IndexError:
#                 continue

#         elif command == "R":
#             try:
#                 if field[first_index][sec_index+1] == '.':
#                     field[first_index][sec_index] == '.'
#                     sec_index = sec_index + 1
#                     field[first_index][sec_index] == '<'
#                 elif field[first_index][sec_index+1] == '*' or field[first_index][sec_index+1] == '#' or field[first_index][sec_index+1] == '-':
#                     continue
#             except IndexError:
#                 continue

                
#         elif command == 'S':
#             if field[first_index][sec_index] == '^':
#                 try:
#                     for index in reversed(range(first_index)):
#                         if field[index][sec_index] == '.' or field[index][sec_index] == '-':
#                             continue
#                         elif field[index][sec_index] == '*':
#                             field[index][sec_index] == '.'
#                             break
#                         else:
#                             break
#                 except IndexError:
#                     break

#             elif field[first_index][sec_index] == 'v':
#                 try:
#                     for index in range(first_index+1, height):
#                         if field[index][sec_index] == '.' or field[index][sec_index] == '-':
#                             continue
#                         elif field[index][sec_index] == '*':
#                             field[index][sec_index] == '.'
#                             break
#                         else:
#                             break
#                 except IndexError:
#                     break

#             elif field[first_index][sec_index] == '<':
#                 try:
#                     for index in reversed(range(sec_index)):
#                         if field[first_index][index] == '.' or field[first_index][index] == '-':
#                             continue
#                         elif field[first_index][index] == '*':
#                             field[first_index][index] == '.'
#                             break
#                         else:
#                             break
#                 except IndexError:
#                     break

#             elif field[first_index][sec_index] == '>':
#                 try:
#                     for index in range(sec_index+1, width):
#                         if field[first_index][index] == '.' or field[first_index][index] == '-':
#                             continue
#                         elif field[first_index][index] == '*':
#                             field[first_index][index] == '.'
#                             break
#                         else:
#                             break
#                 except IndexError:
#                     break
#     print(f'#{case+1}', end = " ")
#     for i in field:
#         for j in i:
#             print(j, end="")
#         print()

T = int(input())
def tank():
    for h in range(H):
        for w in range(W):
            if maps[h][w] == '<' or maps[h][w] == '>' or maps[h][w] == '^' or maps[h][w] == 'v':
                return h, w
 
def game(a):
    h, w = tank()
    if a == 'U':
        maps[h][w] = '.'
        if h-1 >= 0 and maps[h-1][w] == '.':
            maps[h-1][w] = '^'
        else:
            maps[h][w] = '^'
    if a == 'D':
        maps[h][w] = '.'
        if h+1 < H and maps[h+1][w] == '.':
            maps[h+1][w] = 'v'
        else:
            maps[h][w] = 'v'
    if a == 'L':
        maps[h][w] = '.'
        if w-1 >= 0 and maps[h][w-1] == '.':
            maps[h][w-1] = '<'
        else:
            maps[h][w] = '<'
    if a == 'R':
        maps[h][w] = '.'
        if w+1 < W and maps[h][w+1] == '.':
            maps[h][w+1] = '>'
        else:
            maps[h][w] = '>'
    if a == 'S':
        shoot(h, w, maps[h][w])
     
def shoot(h, w, direct):
    global maps
    if direct == '>':
        if w+1 >= W:
            return
        if maps[h][w+1] == '*':
            maps[h][w+1] = '.'
            return
        if maps[h][w+1] == '#':
            return
        shoot(h, w+1, direct)
                  
    elif direct == '<':
        if w-1 < 0:
            return
        if maps[h][w-1] == '*':
            maps[h][w-1] = '.'
            return
        if maps[h][w-1] == '#':
            return
        shoot(h, w-1, direct)
 
    elif direct == '^':
        if h-1 < 0:
            return
        if maps[h-1][w] == '*':
            maps[h-1][w] = '.'
            return
        if maps[h-1][w] == '#':
            return
        shoot(h-1, w, direct)
     
    elif direct == 'v':
        if h+1 >= H:
            return
        if maps[h+1][w] == '*':
            maps[h+1][w] = '.'
            return
        if maps[h+1][w] == '#':
            return
        shoot(h+1, w, direct)
    
     
for case in range(1, T+1):
    H, W = map(int, input().split())
    maps = []
    for h in range(H):
        maps.append(list(input()))
    N = int(input())
    action = list(input())
    for a in action:
        game(a)
    print(f'#{case} ', end='')
    for h in range(H):
        for w in range(W):
            print(maps[h][w], end='')
        print()