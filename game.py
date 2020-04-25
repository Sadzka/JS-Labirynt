from sfml import sf

from window import Window
from image import Image
from button import Button


class Game:

    clearColor = sf.Color(0, 0, 0)
    window = Window( 1060, 960 )
    clock = sf.Clock()
    def __init__(self):
        self.wall = Image("wall")
        self.way = Image("way")
        self.start = Image("start")
        self.end = Image("end")
        self.button_generate = Button("Generate", 80, 32)
        self.button_generate.setPosition( 960, 100)
        pass
    
    def getWindow(self):
        return self.window
        
    def update(self):
        dtime = self.clock.restart()
        self.window.update(dtime)
        pass
        
    def render(self):
    
        wind = self.window.getRenderWindow()
        
        # clear the window
        wind.clear( self.clearColor )
        
        # draw content
        for i in range(32):
            self.wall.setPosition(i*32, i*32)
            self.wall.draw( wind )
        
        self.button_generate.draw( wind )
        
        # display window
        wind.display()