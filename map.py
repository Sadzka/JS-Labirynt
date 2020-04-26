from sfml import sf

class Map:

    __tilesizex = 0
    __tilesizey = 0
    __wsizex = 0
    __wsizey = 0
    __sizex = 0
    __sizey = 0
    
    def __init__(self, wsize):
        self.__wsizex, self.__wsizey = wsize
        self.__wsizex = self.__wsizex - 100
    
    
    def generate(self, sizex, sizey):
        self.__sizex = sizex
        self.__sizey = sizey
        self.__tilesizex = self.__wsizex / self.__sizex
        self.__tilesizey = self.__wsizey / self.__sizey
    
    def getSize(self):
        return (self.__sizex, self.__sizey)
        
    def getTilesSize(self):
        return (self.__tilesizex, self.__tilesizey)