
from art import logo

import random


# Functions

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)

    if len(hand) == 2 and score == 21:
        return 0

    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)

    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "The Dealer has Blackjack. \nYOU LOSE"
    elif user_score == 0:
        return "BlackJack! \nYOU WIN"
    elif user_score > 21:
        return "Bust! \nYOU LOSE"
    elif computer_score > 21:
        return "The Dealer Busted! \nYOU WIN"
    elif user_score > computer_score:
        return f"Your {user_score} beats Dealer's {computer_score}\nYOU WIN"
    else:
        return f"Dealer's {computer_score} beats your {user_score}\nYOU LOSE"
    print("\n")


# Main Loop
def play_game():
    game_over = False
    print(logo)

    # Initialize Karate
    user_cards = []
    computer_cards = []

    # Draw Cards
    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"  Your cards: {user_cards}, Score: {user_score}")
        print(f"  Dealer's first card: {computer_cards[0]}")
        print("\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:

            game_over = True

        else:
            hit_me = input("Enter 1 or 2\n1: 'Hit me!'\n2: 'Pass.'\n")
            if hit_me == "1":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your cards: {user_cards}, Final Score: {user_score}")
    print(f"  Dealer's cards: {computer_cards}, Final Score: {computer_score}")
    print("\n")
    print(compare(user_score, computer_score))
    print("\n")


while input("Play BlackJack? (Enter 1 or 2)\n1: Yes\n2: No\n") == "1":
    play_game()


