# 영준이의 카드 카운팅

test = int(input())

for case in range(test):
    cards = input()
    cards_dict = {'S':0, 'D':0, 'H':0, 'C':0}
    deck = []
    length = len(cards)
    for card in range(length//3):
        deck.append(cards[3*card:3*(card+1)])
    
    if len(set(deck)) != len(deck):
        print(f'#{case+1} ERROR')
    else:
        for index in deck:
            card_name = index[0:1]
            cards_dict[card_name] += 1
        print(f'#{case+1}', end=" ")
        values = cards_dict.values()
        for value in values:
            print(13-value, end=" ")
        print()