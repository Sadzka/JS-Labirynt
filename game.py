from sfml import sf

from window import Window


class Game:

    clearColor = sf.Color(0, 0, 0)
    window = Window( 800, 600 )
    clock = sf.Clock()
    def __init__(self):
        pass
    
    def getWindow(self):
        return self.window
        
    def update(self):
        dtime = self.clock.restart()
        self.window.update(dtime)
        pass
        
    def render(self):
        self.window.getRenderWindow().clear( self.clearColor )
        
        self.window.getRenderWindow().display()