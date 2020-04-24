from sfml import sf
from game import Game

import math
import random

game = Game()

while game.getWindow().isOpen():

    game.update()
    game.render()
    pass
