from sfml import sf

# load the messages font
try:
    font = sf.Font.from_file("fonts/arial.ttf")
except IOError as error:
    print("An error occured: {0}".format(error))
    exit(1)

class Widget:
    
    def __init__(self, x=0, y=0):
        self._position = (x, y)
        self._focused = False
        self._size = (32, 32)
    
    def setPosition(self, x=0, y=0):
        self._position = (x, y)
        self.selfupdate()
        
    def setSize(self, x, y):
        self._size = (x, y)
        self.selfupdate()
    
    def setFocus(self, focused):
        self._focused = focused
    
    def getPosition(self) -> tuple:
        return self._position
        
    def getSize(self) -> tuple:
        return self._size
        
    def isFocused(self):
        return self._focused
    
    # virtual
    def draw(self, window):
        pass
    
    def selfupdate(self):
        pass