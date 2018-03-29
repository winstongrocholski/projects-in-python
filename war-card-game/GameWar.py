class GameWar():

    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def deal(self):
        for i in range(21):
            for player in self.players:
                player.draw(self.deck)

    def play(self, player1, player2):
        for round in range(21):
            player1_card = player1.playCard()
            player2_card = player2.playCard()
            if(player1_card.cardValue() > player2_card.cardValue()):
                print(f'{player1.name} won round {round}')
                player1.win()
            elif(player1_card.cardValue() < player2_card.cardValue()):
                print(f'{player2.name} won round {round}')
                player2.win()
            else:
                print(f'Round {round} was a draw')
