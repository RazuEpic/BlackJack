import random as rd

card_pool = [2, 3, 4, 5, 6, 7, 8, 9, 10]
dlr_choices = ['hit', 'stand']

break_amount = 22

plr_cards = [rd.choice(card_pool)]
dlr_cards = [rd.choice(card_pool)]

while True:
    plr_total = sum(plr_cards)
    dlr_total = sum(dlr_cards)

    plr_turn = input(f'Your Cards: {plr_cards} (Total: {plr_total})\nHit or stand?\n')
    if plr_turn in ['Hit', 'hit', 'H', 'h']:
        random_cards = rd.choice(card_pool)
        plr_cards.append(random_cards)
        print(f'You got {random_cards}')

        if sum(plr_cards) >= break_amount:
            print('The dealer won')
            break
        elif sum(dlr_cards) >= break_amount:
            print('You won')
            break

    elif plr_turn in ['Stand', 'stand', 'S', 's']:
        print(f'Your Cards: {plr_cards} (Total: {sum(plr_cards)})\nYou skipped your turn')

    dlr_turn = rd.choice(dlr_choices)
    if dlr_turn == 'hit':
        random_cards = rd.choice(card_pool)
        dlr_cards.append(random_cards)
        print(f'''Dealer's revealed cards: {dlr_cards[1:]} (Total: {sum(dlr_cards)})''')

    elif dlr_turn == 'stand':
        print('The dealer skips their turn')


    plr_total = sum(plr_cards)
    dlr_total = sum(dlr_cards)
    if plr_total >= break_amount:
        print('The dealer won')
        break
    elif dlr_total >= break_amount:
        print('You won')
        break
