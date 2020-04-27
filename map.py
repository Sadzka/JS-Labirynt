from sfml import sf

class Map:

    __tilesizex = 0
    __tilesizey = 0
    __wsizex = 0
    __wsizey = 0
    __sizex = 0
    __sizey = 0
    
    __map = []
    
    def __init__(self, wsize):
        self.__wsizex, self.__wsizey = wsize
        self.__wsizex = self.__wsizex - 100
    
    
    def generate(self, sizex, sizey):
        self.__map = [ [0 for x in range(0, sizex)] for y in range(0, sizey) ]

        self.__sizex = sizex
        self.__sizey = sizey
        self.__tilesizex = self.__wsizex / self.__sizex
        self.__tilesizey = self.__wsizey / self.__sizey
    
    def getSize(self):
        return (self.__sizex, self.__sizey)
        
    def getTilesSize(self):
        return (self.__tilesizex, self.__tilesizey)
    
    def getMap(self):
        return self.__map