class Stats():

    def __init__(self):
        self.win_count = 0
        self.lost_count = 0

    def win(self):
        self.win_count += 1

    def winCount(self):
        return self.win_count

    def lost(self):
        self.lost_count += 1

    def lostCount(self):
        return self.lost_count


class Player(Stats):

    def __init__(self, name):
        self.hand = []
        self.name = name
        self.win_count = 0

    def draw(self, deck):
        self.hand.append(deck.draw())

    def playCard(self):
        return self.hand.pop()

    def showHand(self):
        for card in self.hand:
            card.show()

    def cardCount(self):
        return len(self.hand)
