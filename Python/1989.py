# 초심자의 회문 검사

test = int(input())

for case in range(test):
    palindrome = input()
    if palindrome == palindrome[::-1]:
        print(f'#{case+1} 1')
    else:
        print(f'#{case+1} 0')
