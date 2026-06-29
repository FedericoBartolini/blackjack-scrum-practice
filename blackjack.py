"""
Simple Blackjack Game - SCRUM Practice Template

Sprint Goal:
Build a basic text-based Blackjack game in Python.

Roles:
- Federico: Scrum Master + Developer + template/integration
- Samrawit Gebru: Deck and cards
- Tshilidzi Violet Masindi: User input and text output
- Aida Hadi Rubio: Product Owner/Client + game logic and winner rules

Simplified rules:
- One human player plays against the computer.
- Use a normal 52-card deck without jokers.
- Ace = 1, cards 2-10 keep their value, J/Q/K = 10.
- The aim is to get as close as possible to 21 without going over.
- The user plays first and chooses to draw or stay.
- The computer reveals its hidden card and draws until its score is > 18.
- If both players have the same score, the computer wins.
"""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------

import random


# ------------------------------------------------------------
# SAMRAWIT GEBRU - DECK AND CARDS
# Add your code in this section.
# ------------------------------------------------------------

def create_deck():
    """
    TODO - Samrawit:
    Create and return a 52-card deck.

    Suggested format:
    ["A", "2", "3", ..., "10", "J", "Q", "K", repeated for 4 suits]
    """
    # Replace this placeholder with your code.
    pass


def shuffle_deck(deck):
    """
    TODO - Samrawit:
    Shuffle the deck and return it.
    """
    # Replace this placeholder with your code.
    pass


def draw_card(deck):
    """
    TODO - Samrawit:
    Remove and return one card from the deck.
    """
    # Replace this placeholder with your code.
    pass


def card_value(card):
    """
    TODO - Samrawit:
    Return the numeric value of one card.
    Ace = 1, J/Q/K = 10.
    """
    # Replace this placeholder with your code.
    pass


# ------------------------------------------------------------
# TSHILIDZI VIOLET MASINDI - USER INPUT AND TEXT OUTPUT
# Add your code in this section.
# ------------------------------------------------------------

def show_start_screen():
    """
    TODO - Tshilidzi:
    Print a simple welcome message and explain the controls.
    """
    # Replace this placeholder with your code.
    pass


def show_hands(user_hand, computer_hand, hide_computer_card=True):
    """
    TODO - Tshilidzi:
    Display the user's cards and the computer's cards.

    If hide_computer_card is True, show the first computer card as [X].
    Example:
    Computer's cards: [X][8]
    User's cards: [4][3] (sum: 7)
    """
    # Replace this placeholder with your code.
    pass


def ask_user_draw():
    """
    TODO - Tshilidzi:
    Ask the user if they want to draw a new card.
    Return True for yes and False for no.
    """
    # Replace this placeholder with your code.
    pass


def show_result(message):
    """
    TODO - Tshilidzi:
    Print the final result message.
    Example: USER WINS! or COMPUTER WINS!
    """
    # Replace this placeholder with your code.
    pass


# ------------------------------------------------------------
# AIDA HADI RUBIO - GAME LOGIC AND WINNER RULES
# Add your code in this section.
# ------------------------------------------------------------

def calculate_score(hand):
    """
    TODO - Aida:
    Calculate and return the total score of a hand.
    Use card_value(card) from Samrawit's section.
    """
    # Replace this placeholder with your code.
    pass


def is_bust(hand):
    """
    TODO - Aida:
    Return True if the hand score is over 21.
    Otherwise return False.
    """
    # Replace this placeholder with your code.
    pass


def computer_should_draw(computer_hand):
    """
    TODO - Aida:
    Return True if the computer score is less than 18.
    Return False if the computer score is 18 or more.
    """
    # Replace this placeholder with your code.
    pass


def decide_winner(user_hand, computer_hand):
    """
    TODO - Aida:
    Decide the winner using the simplified rules.

    Rules:
    - If user goes over 21, computer wins.
    - If computer goes over 21, user wins.
    - If user score is higher than computer score, user wins.
    - If scores are equal, computer wins.
    - Otherwise, computer wins.

    Return a string, for example:
    "USER WINS!" or "COMPUTER WINS!"
    """
    # Replace this placeholder with your code.
    pass


# ------------------------------------------------------------
# TEMPLATE, INTEGRATION, AND MAIN GAME FLOW
# ------------------------------------------------------------

def setup_game():
    """
    Create the deck, shuffle it, and deal two cards to each player.
    """
    deck = create_deck()
    deck = shuffle_deck(deck)

    user_hand = [draw_card(deck), draw_card(deck)]
    computer_hand = [draw_card(deck), draw_card(deck)]

    return deck, user_hand, computer_hand


def user_turn(deck, user_hand, computer_hand):
    """
    Control the user's turn using the input/output and logic functions.
    """
    print("\nUSER'S TURN")

    while True:
        show_hands(user_hand, computer_hand, hide_computer_card=True)

        if is_bust(user_hand):
            return

        if ask_user_draw():
            new_card = draw_card(deck)
            user_hand.append(new_card)
            print(f"User drew [{new_card}]")
        else:
            print("User stays.")
            return


def computer_turn(deck, computer_hand):
    """
    Control the computer's turn using the game logic function.
    """
    print("\nCOMPUTER'S TURN")

    while computer_should_draw(computer_hand):
        new_card = draw_card(deck)
        computer_hand.append(new_card)
        print(f"Computer drew [{new_card}]")

    print("Computer stays.")


def main():
    """
    Main game flow.
    This should work after all team members complete their sections.
    """
    show_start_screen()

    deck, user_hand, computer_hand = setup_game()

    user_turn(deck, user_hand, computer_hand)

    if not is_bust(user_hand):
        computer_turn(deck, computer_hand)

    print("\nEND")
    show_hands(user_hand, computer_hand, hide_computer_card=False)

    result = decide_winner(user_hand, computer_hand)
    show_result(result)


if __name__ == "__main__":
    main()
