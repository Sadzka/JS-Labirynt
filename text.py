from sfml import sf
from widget import Widget
from widget import font

class Text(Widget):
    def __init__(self, text, x=0, y=0):
        super().__init__(x, y)
        
        self.text = sf.Text(text)
        self.text.font = font
        self.text.character_size = 20
        
    def setCharacterSize(size):
        self.text.character_size = size
        
    def getCharacterSize(size) -> int:
        return self.text.character_size
    
    def setText(string):
        self.text.string = string
        
    def getText(string):
        return self.text.string
        
    def draw(self, window):
        window.draw(self.text)
        
    def selfupdate(self):
        self.text.position = self.position
        
    def handleEvent(self, event, window):
        return