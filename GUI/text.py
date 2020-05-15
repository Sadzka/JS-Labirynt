from sfml import sf
from GUI.widget import Widget
from GUI.widget import font

class Text(Widget):

    def __init__(self, text, x=0, y=0):
        super().__init__(x, y)
        
        self._text = sf.Text(text)
        self._text.font = font
        self._text.character_size = 20
        self.__string = text
        
    def setCharacterSize(self, size):
        self._text.character_size = size
        
    def getCharacterSize(self, size) -> int:
        return self._text.character_size
    
    def setText(self, string):
        self.__string = string
        self._text.string = self.__string
        
    def getText(self):
        return self.__string
        
    def draw(self, window):
        window.draw(self._text)
        
    def selfupdate(self):
        self._text.position = self._position