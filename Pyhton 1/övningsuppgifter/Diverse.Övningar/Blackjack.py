import random

# Create a deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
# Shuffle deck
random.shuffle(deck)
player_hand = []
dealers_hand = []
playerIn, dealerIn = True, True

# Create function for dealing cards from deck
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Create function for calculation total score
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    aces = 0
    # Count card as their value, count face cards as 10 & count aces as 11
    for card in turn:
        if card in face:
            total += 10
        elif card == 'A':
            total += 11
            aces += 1
        else:
            total += card
    # If total over 21 convert aces to 1 instead of 11
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

# Reavel only the first card in dealers hand
def revealDealerHand():
    return dealers_hand[0]

# game loop
# Give the player and dealer 2 cards each
for _ in range(2):
    dealCard(dealers_hand)
    dealCard(player_hand)
# If both player and dealer are still in, execute the loop
while playerIn or dealerIn:
    print(f'Dealer has {revealDealerHand()} and X')
    print(f'You have {player_hand} for a total of {total(player_hand)}')
    if playerIn:
        stay_or_hit = input('1: Stay\n2: Hit\n')
        if stay_or_hit == '1':
            playerIn = False
        # If player "Hits" give 1 more card
        elif stay_or_hit == '2':
            dealCard(player_hand)
        else:
            print("Invalid choice. Please select 1 or 2.")
            continue
    # If dealder cars over 16 then fold
    if total(dealers_hand) > 16:
        dealerIn = False
    # Otherwise give dealer a card
    else:
        dealCard(dealers_hand)
    # If either player or dealer has 21 or over, break the loop
    if total(player_hand) >= 21 or total(dealers_hand) >= 21:
        break
#
player_total = total(player_hand)
dealer_total = total(dealers_hand)

# Print out scores
print(f'\nYou have {player_hand} for a total of {player_total}')
print(f'The dealer has {dealers_hand} for a total of {dealer_total}')

if player_total == 21 and dealer_total == 21:
    print('Push! Both you and the dealer have Blackjack.')
elif player_total == 21:
    print('Blackjack! You win!')
elif dealer_total == 21:
    print('Blackjack! Dealer wins!')
elif player_total > 21:
    print('You bust! Dealer wins!')
elif dealer_total > 21:
    print('Dealer bust! You win!')
elif dealer_total > player_total:
    print('Dealer Wins!')
else:
    print('You win!')
