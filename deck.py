from card import Card

class Deck:
    def __init__(self) -> None:
        suites = ["♠", "♥", "♦", "♣"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = list()
        for s in suites:
            for v in values:
                self.deck.append(Card(v, s))

    def take(self, card) -> Card:
        return card

    def remove(self, card) -> None:
        self.deck.remove(card)

    def is_empty(self) -> bool:
        return len(self.deck) == 0