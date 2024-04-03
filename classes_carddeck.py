from random import shuffle

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.suit}{self.rank}'
    
class Deck:
    __SUIT = {'♣': 1, '♢': 2, '♡': 3, '♠': 4}
    __RANK = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    def __init__(self):
        self.d = []
        for i in __class__.__SUIT:
            for j in __class__.__RANK:
                self.d.append(Card(i, j))
                
    def shuffle(self):
        if len(self.d) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.d)
        
    def deal(self):
        if not self.d:
            raise ValueError('Все карты разыграны')
        return self.d.pop()       
    
    def __str__(self):
        return f'Карт в колоде: {len(self.d)}'