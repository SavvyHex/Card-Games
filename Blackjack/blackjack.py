from random import choice
import sys

sys.path.append("../Card Games")

from deck import Deck
from hand import Hand

class Blackjack:
    def __init__(self) -> None:
        self.deck = Deck()
        self.player, self.dealer = Hand(), Hand()

    def drawCard(self, forPlayer:bool=True) -> None:
        if self.deck.is_empty():
            self.deck = Deck()
            print("New deck!")
        card = choice(self.deck.deck)
        if forPlayer:
            self.player.draw(card)
        else:
            self.dealer.draw(card)
        self.deck.remove(card)

    def new_round(self) -> None:
        for i in range(2):
            self.drawCard()
            self.drawCard(False)

        print("Dealer : ")
        print(self.dealer.hand[0])
        print("You : ")
        print(self.player.hand[0], self.player.hand[1])