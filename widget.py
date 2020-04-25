from sfml import sf

# load the messages font
try:
    font = sf.Font.from_file("fonts/arial.ttf")
except IOError as error:
    print("An error occured: {0}".format(error))
    exit(1)

class Widget:
    focused = False
    size = (32, 32)
    position = (0, 0)
    
    def __init__(self, x=0, y=0):
        self.position = (x, y)
    
    def setPosition(self, x=0, y=0):
        self.position = (x, y)
        self.update()
        
    def setSize(self, x, y):
        size = ( x, y)
        self.update()
    
    def setFocused(self, focused):
        self.focused = focused
    
    def getPosition(self) -> tuple:
        return self.position
        
    def getSize(self) -> tuple:
        return self.position
    
    # virtual
    def draw(self, window):
        pass
    
    def update(self):
        pass