# 다솔이의 다이아몬드 장식

test = int(input())

for case in range(test):
    letters = input()
    
    print('..#.' * len(letters), end="")
    print('.')
    for i in range(1,((len(letters)) * 2) + 1):
        print('.#', end="")
    print('.')
    for letter in letters:
        print(f'#.{letter}.', end="")
    print('#')
    for i in range(1,((len(letters)) * 2) + 1):
        print('.#', end="")
    print('.')
    print('..#.' * len(letters), end="")
    print('.')
