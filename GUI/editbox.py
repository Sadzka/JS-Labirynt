from sfml import sf

from GUI.widget import Widget
from GUI.widget import font
from GUI.text import Text

MOUSE_LEFT, MOUSE_RIGHT, MOUSE_MIDDLE = range(3)

class EditBox(Text):

    __caret = sf.Text('|')
    __caret.font = font
    __caret.character_size = 20
    
    def __init__(self, x=0, y=0, sizex=32, sizey=32, text=""):
        """
        Create a EditBox object.
        Parameters:
        x (int) : position of left corner
        y (int) : position of upper corner
        sizex (int) : width of EditBox
        sizey (int) : height of EditBox
        text (str) : text in button
        """
        super().__init__(text, x, y)
        self.__canvas = sf.RenderTexture(sizex, sizey)
        self.__sprite = 0
        self._text.position = (5, 0)
          
    def draw(self, window):
        """
        Draw this widget in window.
        Parameters:
        window (Window) : Window to draw.
        """
        self.__canvas.clear( sf.Color(155, 155, 155) )
        
        self.__canvas.draw(self._text)

        #caret
        if self._focused:
            if self._elapsed_time < 0.5:
                self.__caret.position = (self._text.position.x + self._text.global_bounds.width, self._text.position.y)
                self.__canvas.draw(self.__caret)
            if self._elapsed_time > 1.0:
                self._elapsed_time = self._elapsed_time - 1.0

        self.__canvas.display()
                
        self.__sprite = sf.Sprite(self.__canvas.texture)
        self.__sprite.position = self._position
        window.draw(self.__sprite)
        
    def selfupdate(self):
        pass
        
    def handle_event(self, event, mousepos, GUI):
        """
        Handle window event.
        
        Parameters:
        event (sf.Event) : Event to handle.
        mousepos (int, int) : Position of mouse.
        GUI (GUIManager) : GUIManager with widgets.
        """
        
        if self.__sprite == 0:
            return
            
        if self.__sprite.global_bounds.contains(mousepos):        
            if event == sf.Event.MOUSE_BUTTON_RELEASED:
                if event['button'] ==  MOUSE_LEFT:
                    GUI.focus_me(self)
                    
        if(self._focused):
            if event == sf.Event.TEXT_ENTERED:
            
                #Backspace
                if event['unicode'] == '\u0008':
                    self.set_text(self.get_text()[:-1])
                    
                #Escape, Tab, Enter
                elif event['unicode'] == '\u001B' or event['unicode'] == '\u000D' or event['unicode'] == '\u0009':
                    self.set_focus(False)
                else:
                    self.set_text(self.get_text() + event['unicode'])
                