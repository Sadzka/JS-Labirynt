from sfml import sf
from game import Game
from GUI.errorshower import ErrorshowerException
from GUI.errorshower import Errorshower as ES

game = Game()

while game.getWindow().isOpen():

    try:
        game.update()
        game.render()
    except ErrorshowerException as exc:
        ES.show( exc.getValue() )
        