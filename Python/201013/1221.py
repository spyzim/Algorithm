# GNS
test = int(input())

for test_case in range(1, test + 1):
    case_num, length = input().split()
    num = list(input().split())
    length = int(length)

    alien_num = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN": 7, "EGT" : 8, "NIN": 9}
    human_num = {v:k for k,v in alien_num.items()}

    for index in range(length):
        num[index] = alien_num[num[index]]
    
    num.sort()

    print(case_num)
    for i in num:
        print(i, end = " ")
    print()
