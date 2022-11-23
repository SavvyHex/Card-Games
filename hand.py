from card import Card

class Hand():
    def __init__(self, name:str) -> None:
        self.name = name
        self.hand = list()

    def draw(self, card:Card) -> None:
        self.hand.append(Card)

    def remove(self, card:Card) -> None:
        self.hand.remove(Card)
