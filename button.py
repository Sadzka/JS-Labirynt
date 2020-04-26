from sfml import sf
from widget import Widget
from widget import font
from text import Text

class Button(Text):
    __leftCallback = 0
    __rightCallback = 0
    def __init__(self, text, x=0, y=0):
        super().__init__(text, x, y)
        
        self.text = sf.Text(text)
        self.text.font = font
        self.text.character_size = 20
        
    
    def draw(self, window):
        window.draw(self.text)
        
    def selfupdate(self):
        self.text.position = self.position
        
    def bindLeftCallback(self, funct):
        self.__leftCallback = funct
        
    def bindRightCallback(self, funct):
        self.__leftCallback = funct
        
    
    def handleEvent(self, event, window):
        mousepos = sf.Mouse.get_position(window)
        if event == sf.Event.MOUSE_MOVED:
            if self.text.global_bounds.contains(mousepos):
                self.text.color = sf.Color(0, 255, 0)
            else:
                self.text.color = sf.Color(255, 255, 255)
                
        if event == sf.Event.MOUSE_BUTTON_RELEASED:
            if event['button'] ==  0:
                if self.__leftCallback != 0:
                    self.__leftCallback()   
            elif event['button'] ==  1:
                if self.__rightCallback != 0:
                   self.__rightCallback()