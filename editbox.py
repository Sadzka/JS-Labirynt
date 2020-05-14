from sfml import sf
from widget import Widget
from widget import font
from text import Text

class EditBox(Text):

    _caret = sf.Text('|')
    _caret.font = font
    _caret.character_size = 20
    
    def __init__(self, x=0, y=0, sizex=32, sizey=32, text="3"):
        super().__init__(text, x, y)
        self._canvas = sf.RenderTexture(sizex, sizey)
        self._sprite = 0
        self._text.position = (5, 0)
        
        
    def draw(self, window):
    
            
        self._canvas.clear( sf.Color(155, 155, 155) )
        
        self._canvas.draw(self._text)

        #caret
        if self._focused:
            if self._elapsedTime < 0.5:
                self._caret.position = ( self._text.position.x + self._text.global_bounds.width, self._text.position.y )
                self._canvas.draw(self._caret)
            if self._elapsedTime > 1.0:
                self._elapsedTime = self._elapsedTime - 1.0

        self._canvas.display()
                
        self._sprite = sf.Sprite( self._canvas.texture )
        self._sprite.position = self._position
        window.draw(self._sprite)
        
        
    def selfupdate(self):
        pass
        
    def handleEvent(self, event, mousepos, GUI):
        
        if( self._sprite == 0 ):
            return
            
        if self._sprite.global_bounds.contains(mousepos):        
            if event == sf.Event.MOUSE_BUTTON_RELEASED:
                if event['button'] ==  0:
                    GUI.focusMe( self )
                    
        if(self._focused):
            if event == sf.Event.TEXT_ENTERED:
            
                #backspace
                if event['unicode'] == '\u0008':
                    self.setText( self.getText()[:-1] )
                    
                #escape Tab Enter
                elif event['unicode'] == '\u001B' or event['unicode'] == '\u000D' or event['unicode'] == '\u0009':
                    self.setFocus(False)
                else:
                    self.setText( self.getText() + event['unicode'] )
                