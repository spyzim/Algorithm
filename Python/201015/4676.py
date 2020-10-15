# 늘어지는 소리 만들기

test = int(input())

for case in range(test):
    string = input()
    hyphen_num = int(input())
    hyphen_location = list(map(int, input().split()))
    hyphen_location.sort()
    hyphen_dict = {}

    for i in hyphen_location:
        if i in hyphen_dict.keys():
            hyphen_dict[i] += 1
        else:
            hyphen_dict[i] = 1

    extra_key = 0
    
    for key, value in hyphen_dict.items():
        string = string[ :key + extra_key] + ('-' * value) + string[key + extra_key: ]
        extra_key += value
    print(f'#{case+1} {string}') 
  

# dict = { 1 : 80, 'daum' : 30}
# dict['kakao'] = 50
# print(dict)