import random

# Function to calculate the value of the hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card[:-1]  # Extract the rank from the card (excluding the suit)
        if rank.isdigit():
            value += int(rank)
        elif rank in 'JQK':
            value += 10
        elif rank == 'A':
            num_aces += 1
            value += 11

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value


# Function to display cards
def display_cards(player_hand, dealer_hand):
    print(f"Player's hand: {', '.join(player_hand)}")
    print(f"Dealer's hand: {', '.join(dealer_hand[:-1])}, [Hidden]")

# Initialize the deck
suits = ['H', 'D', 'C', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [rank + suit for suit in suits for rank in ranks]

# Game setup
random.shuffle(deck)
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Display initial cards
display_cards(player_hand, dealer_hand)

# Player's turn
while True:
    player_value = calculate_hand_value(player_hand)
    if player_value == 21:
        print("Blackjack! You win!")
        break
    elif player_value > 21:
        print("Bust! You lose.")
        break

    action = input("Do you want to hit or stand? (h/s): ").lower()
    if action == 'h':
        player_hand.append(deck.pop())
        display_cards(player_hand, dealer_hand)
    else:
        break

# Dealer's turn
dealer_value = calculate_hand_value(dealer_hand)
while dealer_value < 17:
    dealer_hand.append(deck.pop())
    dealer_value = calculate_hand_value(dealer_hand)

# Display final hands
print("\nFinal hands:")
display_cards(player_hand, dealer_hand)

# Determine the winner
if dealer_value > 21:
    print("Dealer busts! You win!")
elif dealer_value == player_value:
    print("It's a tie!")
elif dealer_value > player_value:
    print("Dealer wins!")
else:
    print("You win!")
