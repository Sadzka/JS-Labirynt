from sfml import sf
import collections
import numpy as np
import random

class Map:
    
    #window size
    __wsizex = 0
    __wsizey = 0
    
    __tilesizex = 0
    __tilesizey = 0
    
    __sizex = 0
    __sizey = 0
    
    __map = []
    
    def __init__(self, wsize):
        self.__wsizex, self.__wsizey = wsize
        self.__wsizex = self.__wsizex - 100
        
    def generateGrid(self, x, y):
        
        sizex = 0
        sizey = 0
        
        try:
            sizex = int(x)
        except Exception as ex:
            print('Size X is not a integer')
            return
            
        try:
            sizey = int(y)
        except Exception as ex:
            print('Size Y is not a integer')
            return
    
    
        if sizex < 3 or sizex > 30 or sizey < 3 or sizey > 30:
            print("Zly rozmiar")
            print("TODO")
            return
        
        self.__map = [ [0 for x in range(0, sizex)] for y in range(0, sizey) ]
        """
        for x in range(1, sizex):
            self.__map[x][0] = 1
            self.__map[x][sizey-1] = 1
            
        for y in range(0, sizey):
            self.__map[0][y] = 1
            self.__map[sizex-1][y] = 1
        """
        
        self.__sizex = sizex
        self.__sizey = sizey
        self.__tilesizey = self.__wsizex / self.__sizex
        self.__tilesizex = self.__wsizey / self.__sizey
        
        #print(self.__map)

    def getSize(self):
        return (self.__sizex, self.__sizey)
        
    def getTilesSize(self):
        return (self.__tilesizex, self.__tilesizey)
    
    def getMap(self):
        return self.__map

    def handleMouseClick():
        #TODO
        pass
  
    