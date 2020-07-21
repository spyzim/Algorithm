# 몫과 나머지 출려하기

test = int(input())

# for i in range(test):
#     a, b = map(int, input().split())
#     print('#', i+1, ' ', a//b, ' ', a%b)

result = [' ', ' '] # 결과값 몫 과 나머지를 담을 리스트. 메모리 절약을 위해 미리 2칸만 할당하도록 초기화 한다.

for i in range(test):
    nums = list(map(int, input().split()))  # map() 을 사용해 문자열 리스트 input().split() 를 정수로 변환
                                            # list 를 사용하여 map 객체의 값을 보고, 그 정수를 nums 리스트 에 담는다. 
    a = nums[0]
    b = nums[1]
    result[0] = a//b
    result[1] = a%b
    print(f'#{i+1} {result[0]} {result[1]}')

