# 퍼펙트 셔플

def perfect_shuffle(list, n):
    if n % 2 ==0:
        deck1 = list[0: n//2]
        deck2 = list[n//2: ]
    else:
        deck1 = list[0: (n//2) + 1]
        deck2 = list[(n//2) + 1: ]
    for i in range(1, len(deck2)+ 1):
        deck1.insert((i * 2) -1 , deck2[i-1])
    return deck1

test = int(input())

for case in range(test):
    cards = int(input())
    card_name = list(input().split())

    print(f'#{case+1}', end=' ')
    for i in perfect_shuffle(card_name, cards):
        print(i, end=' ')
    print()
    