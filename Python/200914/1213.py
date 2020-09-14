# String

# 검색을 수행하는 함수
def find(target, str):
    len_of_target = len(target)
    len_of_str = len(str)
    if(len_of_target > len_of_str):
        return 0
    index = str.find(target)        # find 함수는 특정 인덱스 번호를 반환한다.
    if (index != -1):
        str = str[index+len_of_target:]     # 슬라이싱으로 기존 문자열에서 맨 앞에서 특정 문자열까지 잘라내고 재정의
        return 1 + find(target,str)     # 재귀함수 
    return 0        # 더 이상 찾는 문자열이 없으면 0 을 return 한다.
print("")
for case in range(10):
    case_num = input()
    target = input()
    test = input()
    print(f'#{case_num} {find(target, test)}')