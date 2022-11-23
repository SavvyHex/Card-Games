class Card:
    def __init__(self, value:str, suite:str) -> None:
        self.value = value
        self.suite = suite
    
    def __str__(self) -> str:
        return f"{self.value}{self.suite}"

    def __repr__(self) -> str:
        return str(self)