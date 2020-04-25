from sfml import sf
from game import Game

game = Game()

while game.getWindow().isOpen():
    game.update()
    game.render()