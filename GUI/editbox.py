from sfml import sf
from GUI.widget import Widget
from GUI.widget import font
from GUI.text import Text

class EditBox(Text):

    __caret = sf.Text('|')
    __caret.font = font
    __caret.character_size = 20
    
    def __init__(self, x=0, y=0, sizex=32, sizey=32, text="3"):
        super().__init__(text, x, y)
        self.__canvas = sf.RenderTexture(sizex, sizey)
        self.__sprite = 0
        self._text.position = (5, 0)
          
    def draw(self, window):
    
            
        self.__canvas.clear( sf.Color(155, 155, 155) )
        
        self.__canvas.draw(self._text)

        #caret
        if self._focused:
            if self._elapsedTime < 0.5:
                self.__caret.position = ( self._text.position.x + self._text.global_bounds.width, self._text.position.y )
                self.__canvas.draw(self.__caret)
            if self._elapsedTime > 1.0:
                self._elapsedTime = self._elapsedTime - 1.0

        self.__canvas.display()
                
        self.__sprite = sf.Sprite( self.__canvas.texture )
        self.__sprite.position = self._position
        window.draw(self.__sprite)
        
    def selfupdate(self):
        pass
        
    def handleEvent(self, event, mousepos, GUI):
        
        if( self.__sprite == 0 ):
            return
            
        if self.__sprite.global_bounds.contains(mousepos):        
            if event == sf.Event.MOUSE_BUTTON_RELEASED:
                if event['button'] ==  0:
                    GUI.focusMe( self )
                    
        if(self._focused):
            if event == sf.Event.TEXT_ENTERED:
            
                #Backspace
                if event['unicode'] == '\u0008':
                    self.setText( self.getText()[:-1] )
                    
                #Escape, Tab, Enter
                elif event['unicode'] == '\u001B' or event['unicode'] == '\u000D' or event['unicode'] == '\u0009':
                    self.setFocus(False)
                else:
                    self.setText( self.getText() + event['unicode'] )
                