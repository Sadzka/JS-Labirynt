from sfml import sf
from widget import Widget
from widget import font
from text import Text

class Button(Text):
    def __init__(self, x=0, y=0, text="Button"):
        super().__init__(text, x, y)
        __leftCallback = 0
        __rightCallback = 0
        
    def selfupdate(self):
        self._text.position = self._position
        
    def bindLeftCallback(self, funct):
        self.__leftCallback = funct
        
    def bindRightCallback(self, funct):
        self.__leftCallback = funct
    
    def handleEvent(self, event, window, GUI):
        mousepos = sf.Mouse.get_position(window)
        if event == sf.Event.MOUSE_MOVED:
            if self._text.global_bounds.contains(mousepos):
                self._text.color = sf.Color(0, 255, 0)
            else:
                self._text.color = sf.Color(255, 255, 255)
        
        if self._text.global_bounds.contains(mousepos):        
            if event == sf.Event.MOUSE_BUTTON_RELEASED:
                GUI.focusMe(self)
                if event['button'] ==  0:
                    if self.__leftCallback != 0:
                        self.__leftCallback()   
                elif event['button'] ==  1:
                    if self.__rightCallback != 0:
                       self.__rightCallback()