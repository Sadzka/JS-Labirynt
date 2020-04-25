from sfml import sf
from widget import Widget
from widget import font

class Button(Widget):
    def __init__(self, text, xs=32, ys=32, x=0, y=0):
        super().__init__(x, y)
        
        self.text = sf.Text(text)
        self.text.font = font
        self.text.character_size = 20
        
    
    def draw(self, window):
        window.draw(self.text)
        
    def update(self):
        self.text.position = self.position
        pass