# 알파벳을 숫자로 변환

# alp = input()

# for i in range(len(alp)):
#     asci = list(map(int, alp[i]))
#     print(asci[i], end='')

ins = list(input())     # 입력받은 값을 리스트로 변환
 
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  
nums = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'
nums = list(map(int,nums.split()))    # character형 nums를 int형 리스트로 변환.
dicts = {}                             # 딕셔너리 선언
 
for a in range(1, len(alpha)+1):        # 1~26 까지의 반복문
    dicts[alpha[a-1]] = nums[a-1]       # alpha 리스트의 요소와 nums 리스트의 요소를 각각 key 와 value 로 닥셔너리에 추가.
     
result = ''             # 문자열 선언
     
for i in ins:
    result += str(dicts[i]) + ' '       # dics 의 요소를 문자열로 변화한 뒤 result 에 추가
     
print(result)