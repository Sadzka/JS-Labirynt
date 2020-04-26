from sfml import sf

from window import Window
from image import Image
from button import Button
from guimanager import GUIManager
from map import Map

class Game:
    __windowsize = (1060, 960)
    __window = Window( __windowsize )
    __clock = sf.Clock()
    __GuiManager = GUIManager(__window.getRenderWindow())
    __map = Map( __windowsize )
    
    def __init__(self):
    
        self.wall = Image("wall")
        self.way = Image("way")
        self.start = Image("start")
        self.end = Image("end")
        
        button_generate = Button("Generate", 80, 32)
        button_generate.setPosition( 960, 100)
        button_generate.bindLeftCallback( lambda : self.__map.generate(16, 16) )
        self.__GuiManager.addWidget(button_generate)
    
    def getWindow(self):
        return self.__window
        
    def update(self):
        dtime = self.__clock.restart()
        self.__window.update(self.__GuiManager)
        pass
        
    def render(self):
        sizex, sizey = self.__map.getSize()
        tilex, tiley = self.__map.getTilesSize()
        self.wall.setSize(tilex, tiley)
        
        wind = self.__window.getRenderWindow()
        
        # clear the window
        wind.clear( sf.Color(0, 0, 0) )
        
        # draw content
        
        if tilex != 0 or tiley != 0:
            for i in range(sizex):
                self.wall.setPosition(i*tilex, i*tiley)
                self.wall.draw( wind )
        
        self.__GuiManager.draw(wind)
        
        # display window
        wind.display()