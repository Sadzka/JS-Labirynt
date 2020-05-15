from sfml import sf
"""
from image import Image
from button import Button
from guimanager import GUIManager
from editbox import EditBox
"""
import GUI
from window import Window
from map import Map

class Game:
    __windowsize = (1060, 960)
    __window = Window( __windowsize )
    __clock = sf.Clock()
    __map = Map( __windowsize )
    
    __GuiManager = GUI.guimanager.GUIManager(__window.getRenderWindow(), __map)
    
    def __init__(self):
        self.__loadWidgets()
    
    def getWindow(self):
        return self.__window
        
    def update(self):
        dtime = self.__clock.restart().seconds
        
        self.__window.update(self.__GuiManager)
        self.__GuiManager.update(dtime)
        
    def render(self):
        sizex, sizey = self.__map.getSize()
        tilex, tiley = self.__map.getTilesSize()
        
        self.wall.setSize(tilex, tiley)
        self.way.setSize(tilex, tiley)
        self.start.setSize(tilex, tiley)
        self.end.setSize(tilex, tiley)
        self.indirect.setSize(tilex, tiley)
        self.userindirect.setSize(tilex, tiley)
        
        map = self.__map.getMap()
 
        wind = self.__window.getRenderWindow()
        
        # clear the window
        wind.clear( sf.Color(0, 0, 0) )
        
        # draw content
        if tilex != 0 or tiley != 0:
            for i in range(sizex):
                for j in range(sizey):
                    if map[i][j] == 0:
                        self.wall.setPosition(i*tilex, j*tiley)
                        self.wall.draw( wind )
                    elif map[i][j] == 1:
                        self.way.setPosition(i*tilex, j*tiley)
                        self.way.draw( wind )
                    elif map[i][j] == 2:
                        self.start.setPosition(i*tilex, j*tiley)
                        self.start.draw( wind )
                    elif map[i][j] == 3:
                        self.end.setPosition(i*tilex, j*tiley)
                        self.end.draw( wind )
                    elif map[i][j] == 4:
                        self.indirect.setPosition(i*tilex, j*tiley)
                        self.indirect.draw( wind )
                    elif map[i][j] == 5:
                        self.userindirect.setPosition(i*tilex, j*tiley)
                        self.userindirect.draw( wind )
        
        self.__GuiManager.draw(wind)
        
        # display window
        wind.display()
    
    def __loadWidgets(self):
        self.wall = GUI.image.Image("wall")
        self.way = GUI.image.Image("way")
        self.start = GUI.image.Image("start")
        self.end = GUI.image.Image("end")
        self.indirect = GUI.image.Image("indirect")
        self.userindirect = GUI.image.Image("userindirect")
        
        editBox_X = GUI.editbox.EditBox(sizex=96, sizey=28, text="30")
        editBox_X.setPosition(960, 16)
        
        editBox_Y = GUI.editbox.EditBox(sizex=96, sizey=28, text="30")
        editBox_Y.setPosition(960, 60)
        
        button_showgrid = GUI.button.Button(text="Show Grid")
        button_showgrid.setPosition(960, 100)
        button_showgrid.bindLeftCallback( lambda : self.__map.generateGrid( editBox_X.getText(), editBox_Y.getText() ) )
        
        button_generate = GUI.button.Button(text="Generate")
        button_generate.setPosition(960, 150)
        button_generate.bindLeftCallback( lambda : self.__map.generate() )

        button_solve = GUI.button.Button(text="Solve")
        button_solve.setPosition(960, 200)
        button_solve.bindLeftCallback( lambda : self.__map.solveMaze() )
        
        button_clearSolve = GUI.button.Button(text="Clear Solve")
        button_clearSolve.setPosition(960, 250)
        button_clearSolve.bindLeftCallback( lambda : self.__map.clearSolve() )
        button_clearSolve.setCharacterSize(18)
        
        button_clearPoints = GUI.button.Button(text="Clear points")
        button_clearPoints.setPosition(960, 300)
        button_clearPoints.bindLeftCallback( lambda : self.__map.clearPoints() )
        button_clearPoints.setCharacterSize(18)
        
        self.__GuiManager.addWidget(editBox_X)
        self.__GuiManager.addWidget(editBox_Y)
        self.__GuiManager.addWidget(button_showgrid)
        self.__GuiManager.addWidget(button_generate)
        self.__GuiManager.addWidget(button_solve)
        self.__GuiManager.addWidget(button_clearSolve)
        self.__GuiManager.addWidget(button_clearPoints)
        self.__GuiManager.addWidget(GUI.errorshower.Errorshower)