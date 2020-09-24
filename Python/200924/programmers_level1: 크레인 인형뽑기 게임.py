# board 는 2차원 배열
# moves 는 1차원 배열

# 0 0 0 0 0   0.0 0.1 0.2 0.3 0.4
# 0 0 1 0 3   1.0 1.1 1.2 1.3 1.4
# 0 2 5 0 1   2.0 2.1 2.2 2.3 2.4
# 4 2 4 4 2   3.0 3.1 3.2 3.3 3.4
# 3 5 1 3 1   4.0 4.1 4.2 4.3 4.4
# 인형뽑기

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
bucket = [0]
count = 0                                       #인형이 사라진 횟수
length_of_board = len(board[0])                 #인형뽑기 기계의 한 변의 길이
for i in moves:
    for j in range(length_of_board):            

        if board[j][i-1] != 0:                  #i번 째 칸에서 쭈욱 내려가며 인형이 있는지 존재할 때 까지 검사, 있다면... 
            if board[j][i-1] == bucket[-1]:     #이 과정에서 최초 bucket 이 비어있는 리스트이면 작동하지 않아 0 을 넣어줌. bucket 맨 위의 인형과 이제 들어가는 인형이 같은지 검사
                bucket.remove(board[j][i-1])    #같은 인형이 인접해 만났을 경우 그 인형은 사라진다.
                board[j][i-1] = 0               #인형뽑기 기계에서 뽑힌 인형은 없애준다.
                count += 1
                break                           #인형이 한 개 뽑혔으므로, 해당 i 에서의 for문은 탈출. 새로운 i 를 받으러 간다.
            else:                               #bucket 의 마지막 인형과 들어가는 인형이 같지 않다면..
                bucket.append(board[j][i-1])    #bucket 에 들어가는 인형을 추가해 준다.
                board[j][i-1] = 0
                break

print(count * 2)