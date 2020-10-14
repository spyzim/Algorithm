# 의석이의 세로로 말해요

test = int(input())

for case in range(test):
    words = []
    for i in range(5):
        word = list(input())
        words.append(word)

    max = 0
    for i in words:
        if len(i) > max:
            max = len(i)
    
    new_word = []
    for i in range(max):
        for j in range(5):
            try:
                new_word.append(words[j][i])
            except IndexError:
                continue
    
    print(f'#{case + 1}', end = ' ')
    for i in new_word:
        print(i, end = '')
    print()

