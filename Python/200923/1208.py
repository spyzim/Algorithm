# Flatten

# dump 해주는 함수: 매개변수 자리에 들어온 리스트의 최대값 요소는 -1, 최소값 요소는 +1
# def dump(list):
#     maxValue = max(list)
#     minValue = min(list)
#     for idx in list:
#         if list[idx] == maxValue:
#             list[idx] -= 1
#         elif list[idx] == minValue:
#             list[idx] += 1    
#     return list

# main문
for test_case in range(10):
    dump_num = int(input())
    height = list(map(int, input().split()))
    height.sort()
    for i in range(dump_num):
        if height[99] - height[0] == 1:
            break
        height[0] += 1
        height[99] -= 1
        height.sort()
    print(f'#{test_case + 1} {height[99] - height[0]}')
