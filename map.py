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
    __points = []
    
    def __init__(self, wsize):
        self.__wsizex, self.__wsizey = wsize
        self.__wsizex = self.__wsizex - 100
    
    def generate(self):
        
        #start point
        start = (0, 0)
        
        x, y = start
        
        pk = []
        self.__map = [ [0 for y in range(0, self.__sizey)] for x in range(0, self.__sizex) ]
        self.__map[x][y] = 1
        ways = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        self.__points.append( (start[0], start[1]) )
        while True:
            random.shuffle(ways)
                    
            for dir in ways:
                tx, ty = x + dir[0], y + dir[1]
                
                if 0 <= tx < self.__sizex and 0 <= ty < self.__sizey and self.__map[tx][ty] == 0:
                    end = False
                    
                    for dir2 in ways:
                        ux, uy = tx + dir2[0], ty + dir2[1]
                        
                        if x == ux and y == uy: #pozycja startowa
                            continue
                            
                        if 0 <= ux < self.__sizex and 0 <= uy < self.__sizey:
                            if self.__map[ux][uy] != 0:
                                end = True
                                break
                               
                    if end != True:
                        x, y = tx, ty
                        
                        self.__map[tx][ty] = 1
                        pk.append( (x, y) )
                        self.__points.append( (x, y) )
                        break
                
            else:
                if len(pk) <= 0:
                    break
                x, y = pk.pop()
        pass
        
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
        
        self.__map = [ [0 for y in range(0, sizey)] for x in range(0, sizex) ]
        
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

    def handleMouseClick():
        #TODO
        pass
  
    