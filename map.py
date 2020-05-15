from sfml import sf
import collections
import numpy as np
import random
from GUI.errorshower import ErrorshowerException

class Map:
    
    # Window Size
    __wsizex = 0
    __wsizey = 0
    
    # Tile Size
    __tilesizex = 0
    __tilesizey = 0
    
    # Numbers of rows and columns
    __sizex = 0
    __sizey = 0
    
    # Maze
    __map = []
    
    # User points
    __userpp = []
    
    def __init__(self, wsize):
        self.__wsizex, self.__wsizey = wsize
        self.__wsizex = self.__wsizex - 100
        self.__generated = False
        self.__start = (0, 0)
        self.__end = (2, 2)
        self.__emptyGrid = True
    
    def __checkfield(self, x, y):
        if 0 <= x < self.__sizex and 0 <= y < self.__sizey:
            if self.__map[x][y] != 0:
                return True
        return False
    
    def __checkIfPossible(self):
        ways = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        
        sx, sy = self.__start
        ex, ey = self.__end
        
        for dir in ways:
            tx, ty = sx + dir[0], sy + dir[1]
            if tx == ex and ty == ey:
                return False
        return True

    def __findway(self, pk, ways):
        random.shuffle(ways)     
        for dir in ways:
            tx, ty = self.__x + dir[0], self.__y + dir[1]
            if 0 <= tx < self.__sizex and 0 <= ty < self.__sizey and self.__map[tx][ty] == 0:
                end = False
                
                for dir2 in ways:
                
                    if end:
                        break
                        
                    ux, uy = tx + dir2[0], ty + dir2[1]
                        
                    if self.__x == ux and self.__y == uy: #pozycja startowa
                        continue
                        
                    if self.__checkfield(ux, uy):
                        end = True
                        break
                            
                    
                    
                    if dir == (1, 0):   
                        ux, uy = tx + 1, ty + 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                            
                        ux, uy = tx + 1, ty - 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                                
                                
                    if dir == (0, 1):
                        ux, uy = tx + 1, ty + 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                            
                        ux, uy = tx - 1, ty + 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                                
                    if dir == (0, -1):
                        ux, uy = tx + 1, ty - 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                            
                        ux, uy = tx - 1, ty - 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                                
                                
                    if dir == (-1, 0):
                        ux, uy = tx - 1, ty + 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                                
                        ux, uy = tx - 1, ty - 1
                        if self.__checkfield(ux, uy):
                            end = True
                            break  
                    
                if end != True:
                    self.__x, self.__y = tx, ty
                    
                    self.__map[tx][ty] = 1
                    pk.append( (tx, ty) )
                    self.__points.append( (tx, ty) )
                    break
        else:
            if len(pk) <= 0:
                return True
            self.__x, self.__y = pk.pop()
    
    def __checkNeighbor(self, pk, ways):
        toCheck = [ (1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        for point in toCheck:
            if self.__x + point[0] == self.__end[0] and self.__y + point[1] == self.__end[1]:
            
                random.shuffle(ways)     
                for dir in ways:
                    tx, ty = self.__x + dir[0], self.__y + dir[1]
                    if 0 <= tx < self.__sizex and 0 <= ty < self.__sizey and self.__map[tx][ty] == 0:
                        
                        for dir2 in ways:
                                
                            ux, uy = tx + dir2[0], ty + dir2[1]
                                
                            if self.__x == ux and self.__y == uy: #pozycja startowa
                                continue
                                
                            if 0 <= ux < self.__sizex and 0 <= uy < self.__sizey:
                                if self.__map[ux][uy] != 0 or self.__map[ux][uy] == 3:
                                    end = True
                                    break
                            
                        self.__x, self.__y = tx, ty
                        
                        self.__map[tx][ty] = 1
                        pk.append( (tx, ty) )
                        self.__points.append( (tx, ty) )
                        break
        
    def __connectEnd(self, ways):
        x, y = self.__end[0], self.__end[1]
        
        # Sprawdza czy już nie jest połączony
        for dir in ways:
            tx, ty = x + dir[0], y + dir[1]
            if 0 <= tx < self.__sizex and 0 <= ty < self.__sizey:
                if self.__map[tx][ty] == 1:
                    return
                    
        # Uniemozliwia znalezienie drogi w lini prostej
        if self.__start[1] == self.__end[1]: # Ta sama linia w X
            if self.__start[1] < self.__end[1]:
                ways.remove( (1, 0) )
            else:
                ways.remove( (-1, 0) )
        elif self.__start[0] == self.__end[0]: # Ta sama linia w Y
            if self.__start[0] < self.__end[0]:
                ways.remove( (0, 1) )
            else:
                ways.remove( (0, -1) )
        # Szuka drogi
        for dir in ways:
                             
            tx, ty = x + dir[0], y + dir[1]
            ux, uy = tx + dir[0], ty + dir[1]
            lx, ly = tx + dir[1], ty + dir[0]
            rx, ry = tx - dir[1], ty - dir[0]
            
            if 0 <= ux < self.__sizex and 0 <= uy < self.__sizey:
                if self.__map[ux][uy] != 0:
                
                    if 0 <= lx < self.__sizex and 0 <= ly < self.__sizey:
                        if self.__map[lx][ly] != 0:
                            continue
                            
                    if 0 <= rx < self.__sizex and 0 <= ry < self.__sizey:
                        if self.__map[rx][ry] != 0:
                            continue
                    
                    self.__map[tx][ty] = 1
                    self.__points.append( (tx, ty) )
                    return True
        return False
                    
    def generate(self):
    
        if self.__generated == False:
            raise ErrorshowerException( "Pierwsze wygeneruj siatke" )
            return
        
        if self.__start == self.__end:
            raise ErrorshowerException( "Start nie moze byc na końcu labiryntu" )
            return
            
        if self.__checkIfPossible() == False:
            raise ErrorshowerException( "Nie mozna wygenerowac Labiryntu" )
            return
            
        self.__x, self.__y = self.__start
        
        pk = [ (self.__x, self.__y)]
        self.__points = []
        self.__map = [ [0 for y in range(0, self.__sizey)] for x in range(0, self.__sizex) ]
        self.__map[ self.__x ][ self.__y ] = 2
        self.__map[ self.__end[0] ][ self.__end[1] ] = 3
        self.__points.append( (self.__start[0], self.__start[1]) )
        
        # Pierwsza iteracja, uniemożliwienia korytarza w lini prostej
        ways = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        if len( self.__points ) == 1:
            if self.__start[1] == self.__end[1]: # Ta sama linia w X
                if self.__start[1] < self.__end[1]:
                    ways.remove( (1, 0) )
                else:
                    ways.remove( (-1, 0) )
            elif self.__start[0] == self.__end[0]: # Ta sama linia w Y
                if self.__start[0] < self.__end[0]:
                    ways.remove( (0, 1) )
                else:
                    ways.remove( (0, -1) )
                
        
        ways = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        
        # Generuje pierwsze pole, jeżeli start i koniec są obok siebie
        self.__checkNeighbor(pk, ways)
        
        while True:
            if self.__findway(pk, ways) == True:
                break
        
        # Połącz koniec z labiryntem
        # Jeżeli sie nie udalo, generuj ponownie
        if self.__connectEnd(ways) == False:
            self.generate()
        
        self.__emptyGrid = False
        self.__userpp.clear()
              
    def solveMaze(self):
        if self.__emptyGrid:
            raise ErrorshowerException( "Pierwsze wygeneruj labirynt" )
            return
        self.clearSolve()
        self.__userpptmp = self.__userpp.copy()
        self.__userpptmp.append( self.__end )
        
        wasHere = [ [0 for y in range(0, self.__sizey)] for x in range(0, self.__sizex) ]
        correctPath = [ [0 for y in range(0, self.__sizey)] for x in range(0, self.__sizex) ]
        
        for i in range( len(self.__userpp) + 1):
            self.__recursiveSolve( self.__start, wasHere, correctPath);
            wasHere = [ [0 for y in range(0, self.__sizey)] for x in range(0, self.__sizex) ]
        
        #update
        for x in range(self.__sizex):
            for y in range(self.__sizey):
                if self.__map[x][y] == 1 and correctPath[x][y] == True:
                    self.__map[x][y] = 4
        
        for pos in self.__userpp:
            self.__map[pos[0]][pos[1]] = 5
    
    def __recursiveSolve( self, pos, wasHere, correctPath ):
    
        x, y = pos[0], pos[1]
        
        if len(self.__userpptmp) == 1:
            if pos in self.__userpptmp:
                return True; # If you reached the end
                
        
        if pos in self.__userpptmp:
            correctPath[x][y] = True
            self.__userpptmp.remove(pos)
            return True
            
        elif self.__map[x][y] == 0 or wasHere[x][y]:
            return False;  # If you are on a wall or already were here
            #return True
        
        #if x == self.__end[0] and y == self.__end[1]:
        #    return True; # If you reached the end
            
            
        wasHere[x][y] = True
        
        if x != 0:                                                         # Checks if not on left edge
            if self.__recursiveSolve( (x - 1, y), wasHere, correctPath):   # Recalls method one to the left
                correctPath[x][y] = True
                return True

        if  x != self.__sizex - 1:                                         # Checks if not on right edge
            if self.__recursiveSolve( (x + 1, y), wasHere, correctPath):   # Recalls method one to the right
                correctPath[x][y] = True
                return True
            
        if y != 0:
            if self.__recursiveSolve( (x, y - 1), wasHere, correctPath):   # Recalls method one up
                correctPath[x][y] = True
                return True
                
        if y != self.__sizey - 1:        # Checks if not on bottom edge
            if self.__recursiveSolve( (x, y + 1), wasHere, correctPath):   # Recalls method one down
                correctPath[x][y] = True
                return True
            
        return False
    
    def clearSolve(self):
        self.__map = [ [1 if self.__map[x][y] == 4 else self.__map[x][y] for y in range(0, self.__sizey) ] for x in range(0, self.__sizex) ]
        
    def clearPoints(self):
        self.__userpp.clear()
        self.__map = [ [1 if self.__map[x][y] == 5 else self.__map[x][y] for y in range(0, self.__sizey) ] for x in range(0, self.__sizex) ]

    def setStart(self, x, y):
        if 0 <= x < self.__sizex and 0 <= y < self.__sizey:
            self.__map[ x ][ y ] = 2
            self.__start = (x, y)
        else:
            self.__map[ 0 ][ 0 ] = 2
            self.__start = (0, 0)
            
    def setEnd(self, x, y):
        if 0 <= x < self.__sizex and 0 <= y < self.__sizey:
            self.__map[ x ][ y ] = 3
            self.__end = (x, y)
        else:
            self.__map[ self.__sizex - 1 ][ self.__sizey - 1 ] = 3
            self.__end = (self.__sizex - 1, self.__sizey - 1)
    
    def generateGrid(self, x, y):
        
        sizex = 0
        sizey = 0
        
        try:
            sizex = int(x)
        except Exception as ex:
            raise ErrorshowerException( "Size X nie jest liczba!" )
            return
            
        try:
            sizey = int(y)
        except Exception as ex:
            raise ErrorshowerException( "Size Y nie jest liczba!" )
            return
    
    
        if sizex < 3 or sizex > 30 or sizey < 3 or sizey > 30:
            raise ErrorshowerException( "Dozwolony rozmiar labiryntu wynosi od 3x3 do 30x30" )
            return
        
        self.__map = [ [0 for y in range(0, sizey)] for x in range(0, sizex) ]
        
        self.__sizex = sizex
        self.__sizey = sizey
        self.__tilesizex = self.__wsizex / self.__sizex
        self.__tilesizey = self.__wsizey / self.__sizey
        self.__generated = True
        self.__emptyGrid = True
        self.__userpp.clear()
        
        self.setStart(self.__start[0], self.__start[1])
        self.setEnd(self.__end[0], self.__end[1])

    def getSize(self):
        return (self.__sizex, self.__sizey)
        
    def getTilesSize(self):
        return (self.__tilesizex, self.__tilesizey)
    
    def getMap(self):
        return self.__map

    def __mouseposToTile(self, mousepos):
        return ( int( mousepos.x / self.__tilesizex ), int( mousepos.y / self.__tilesizey ))
    
    def handleEvent(self, event, mousepos):
        if self.__generated == False:
            return
            
        if event == sf.Event.MOUSE_BUTTON_RELEASED:
            if 0 < mousepos.x < self.__wsizex and 0 < mousepos.y < self.__wsizey:
                if event['button'] == 0 and self.__emptyGrid == True:  # Left Mouse
                    self.__map[ self.__start[0] ][ self.__start[1] ] = 0
                    self.__start = self.__mouseposToTile(mousepos)
                    self.__map[ self.__start[0] ][ self.__start[1] ] = 2
                    
                    self.__map[ self.__end[0] ][ self.__end[1] ] = 3
                    
                
                if event['button'] == 1 and self.__emptyGrid == True:  # Right Mouse
                    self.__map[ self.__end[0] ][ self.__end[1] ] = 0
                    self.__end = self.__mouseposToTile(mousepos)
                    self.__map[ self.__end[0] ][ self.__end[1] ] = 3
                    
                    self.__map[ self.__start[0] ][ self.__start[1] ] = 2
                
                if event['button'] == 2 and self.__emptyGrid == False:  # Middle Mouse
                    pos = self.__mouseposToTile(mousepos)
                    if self.__map[ pos[0] ][ pos[1] ] == 5 or self.__map[ pos[0] ][ pos[1] ] == 4:
                        self.__map[ pos[0] ][ pos[1] ] = 1
                        if pos in self.__userpp:
                            self.__userpp.remove( (pos[0], pos[1]) )
                    elif self.__map[ pos[0] ][ pos[1] ] == 1:
                        self.__map[ pos[0] ][ pos[1] ] = 5
                        self.__userpp.append( (pos[0], pos[1]) )
                    #print( self.__userpp )
    