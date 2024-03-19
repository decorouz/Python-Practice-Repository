from dataclasses import dataclass, field
from collections import namedtuple


@dataclass
class PlayingCard:
    rank: str
    suit: str


# You want to give a default value to the deck
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


def make_french_deck() -> list[PlayingCard]:
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: list[PlayingCard] = field(default_factory=make_french_deck)


# A simple deck containing two cards can be created like this
queen_of_hearts = PlayingCard("Q", "Hearts")
ace_of_spades = PlayingCard("A", "Spades")
two_cards = Deck([queen_of_hearts, ace_of_spades])
