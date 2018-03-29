from Deck import Deck
from Player import Player
from GameWar import GameWar


winston = Player('Winston')
marian = Player('Marian')

deck = Deck()
deck.shuffle()

warGame = GameWar([winston, marian], deck)
warGame.deal()
warGame.play(winston, marian)

print('GAME OVER')
print(f'{winston.name} won {winston.winCount()} Rounds.')
print(f'{marian.name} won {marian.winCount()} Rounds.')
