from sfml import sf

# load the messages font
try:
    font = sf.Font.from_file("fonts/arial.ttf")
except IOError as error:
    print("An error occured: {0}".format(error))
    exit(1)

class Widget:
    __focused = False
    size = (32, 32)
    position = (0, 0)
    
    def __init__(self, x=0, y=0):
        self.position = (x, y)
    
    def setPosition(self, x=0, y=0):
        self.position = (x, y)
        self.selfupdate()
        
    def setSize(self, x, y):
        self.size = (x, y)
        self.selfupdate()
    
    def setFocused(self, focused):
        self.__focused = focused
    
    def getPosition(self) -> tuple:
        return self.position
        
    def getSize(self) -> tuple:
        return self.position
        
    def isFocused():
        return __focused
    
    # virtual
    def draw(self, window):
        pass
    
    def selfupdate(self):
        pass