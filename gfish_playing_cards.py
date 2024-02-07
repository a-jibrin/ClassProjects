
"""
This module will provide classes for working with a standard deck of playing cards.
The classes are Card and Deck, which allow you to create, represent, and manipulate playing cards and decks of cards.

Classes:
    - Card: Represents an individual playing card.
    - Deck: Represents a deck of playing cards.

Usage:
    These classes can be used to create decks of cards, draw cards from the deck, and work with individual playing cards for various card games.
"""

import re
from random import shuffle

class Card:
    """
    Represents an individual playing card with attributes for suit, value, and name.

    Attributes:
        - suit (str): The suit of the card, such as "Clubs", "Diamonds", "Hearts", or "Spades".
        - value (int): The numeric value of the card (2 to 14, where 11 = Jack, 12 = Queen, 13 = King, and 14 = Ace).
        - name (str): The name of the card, derived from its value ("2" to "10", "Jack", "Queen", "King", or "Ace").

    Methods:
        - __init__(self, value, suit): Initializes a Card object with the specified value and suit.
        - __str__(self): Returns a string representation of the card in the format "<name> of <suit>".

    Usage:
         Card objects to represent individual playing cards created; using their attributes and methods to retrieve information about the card.

    """

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        self.name = self.get_card_name()

    def get_card_name(self):
        value_names = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace",}
        
        if self.value in value_names:
            return value_names[self.value]
        elif 2 <= self.value <= 10:
            return str(self.value)
        else:
            raise ValueError("Invalid card value")

    def __str__(self):
        return f"{self.name} of {self.suit}"

class Deck:
    """
    Represents a deck of playing cards.

    Attributes:
        - cards (list): A list of Card objects representing the entire deck of playing cards.

    Methods:
        - __init__(self): Initializes a Deck object with a complete set of 52 playing cards, including all suits and values, and shuffles the deck.
        - draw(self): Draws a card from the deck, removing it from the deck and returns it.
    
    Usage:
        Deck objects to represent a standard deck of playing cards, shuffling the deck, and drawing cards from it in card games.

    """
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(2, 15):
                card = Card(value, suit)
                self.cards.append(card)
        shuffle(self.cards)

    def draw(self):
        if not self.cards:
            raise RuntimeError("The deck is empty")
        return self.cards.pop()
