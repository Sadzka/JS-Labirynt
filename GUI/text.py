from sfml import sf

from GUI.widget import Widget
from GUI.widget import font

class Text(Widget):
    """Widget to show text."""
    def __init__(self, text, x=0, y=0):
        """
        Create a Text object.
        Parameters:
        text (str) : text in button
        x (int) : position of left corner
        y (int) : position of upper corner
        """
        super().__init__(x, y)
        
        self._text = sf.Text(text)
        self._text.font = font
        self._text.character_size = 20
        self.__string = text
        
    def set_character_size(self, size):
        self._text.character_size = size
        
    def get_character_size(self, size) -> int:
        return self._text.character_size
    
    def set_text(self, string):
        self.__string = string
        self._text.string = self.__string
        
    def get_text(self):
        return self.__string
        
    def draw(self, window):
        """
        Draw this widget in window.
        
        Parameters:
            window (Window) : Window to draw.
        """
        window.draw(self._text)
        
    def selfupdate(self):
        self._text.position = self._position