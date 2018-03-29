import random

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        return  "{0} of {1}".format(self.value,self.suit)

    def cardValue(self):
        if(self.value == 'A'):
            return 14
        elif(self.value == 'J'):
            return 11
        elif(self.value == 'Q'):
            return 12
        elif(self.value == 'K'):
            return 13
        else:
            return self.value

class Deck():

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()
