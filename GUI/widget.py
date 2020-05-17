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
        self._elapsed_time = 0
    
    def set_position(self, x=0, y=0):
        self._position = (x, y)
        self.selfupdate()
        
    def set_size(self, x, y):
        self._size = (x, y)
        self.selfupdate()
    
    def set_focus(self, focused):
        self._focused = focused
    
    def get_position(self) -> tuple:
        return self._position
        
    def get_size(self) -> tuple:
        return self._size
        
    def is_focused(self):
        return self._focused
        
    def update(self, time):
        self._elapsed_time += time
    
    # virtual
    def draw(self, window):
        pass
    
    def selfupdate(self):
        pass