from random import choice
import sys

sys.path.append("../Card Games")

from deck import Deck
from hand import Hand

class Blackjack:
    def __init__(self) -> None:
        self.deck = Deck()
        self.player, self.comp = Hand(), Hand()

    def drawCard(self, forPlayer:bool=True) -> None:
        if self.deck.is_empty():
            self.deck = Deck()
        card = choice(self.deck.deck)
        if forPlayer:
            self.player.draw(card)
        else:
            self.comp.draw(card)
        self.deck.remove(card)