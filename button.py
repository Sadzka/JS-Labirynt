from sfml import sf
from widget import Widget
from widget import font
from text import Text

class Button(Text):
    def __init__(self, text, x=0, y=0):
        super().__init__(text, x, y)
        
        self.text = sf.Text(text)
        self.text.font = font
        self.text.character_size = 20
        
    
    def draw(self, window):
        window.draw(self.text)
        
    def selfupdate(self):
        self.text.position = self.position
    
    def handleEvent(self, event, window):
        mousepos = sf.Mouse.get_position(window)
        if event == sf.Event.MOUSE_MOVED:
            if self.text.global_bounds.contains(mousepos):
                self.text.color = sf.Color(0, 255, 0)
            else:
                self.text.color = sf.Color(255, 255, 255)