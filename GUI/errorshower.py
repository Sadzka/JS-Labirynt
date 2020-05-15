from sfml import sf
from GUI.widget import Widget
from GUI.widget import font
from GUI.text import Text

class ErrorshowerException(Exception):
    def __init__(self,text):
        self.value = text
        
    def getValue(self):
        return self.value

class errorshower(Text):
    
    def __init__(self, x=0, y=0, fontsize=32, duration=2, fade=3, center=True):
    
        if not __name__ == "GUI.errorshower":
            raise "Another instance of this object can't be created"
            
        super().__init__("", x, y)
        self.setCharacterSize(32)
        self._position = (x, y)
        self.__duration = duration
        self.__center = center
        
        if fade < self.__duration:
            self.__fade = self.__duration + 1
        else:
            self.__fade = fade
    
    def selfupdate(self):
        if self.__center:
            self._text.position = ( self._position[0] - self._text.global_bounds.width/2, self._position[1] - self._text.global_bounds.height/2 )
        else:
            self._text.position = ( self._position[0], self._position[1] )

    def setCenter(self, center):
        self.__center = center
        self.selfupdate()
    
    def show(self, str=""):
        if not str == "":
            self.setText(str)
        
        self._elapsedTime = 0
        self._text.color = sf.Color(255, 0, 0, 255);
        self.selfupdate()
        
    def setDuration(self, duration ):
        self.__duration = duration
        
    def setFade(self, fade):
        if fade < self.__duration:
            self.__fade = self.__duration + 1
        else:
            self.__fade = fade
    
    def draw(self, window):
        alpha = 255
        if self._elapsedTime < self.__fade:
            if self._elapsedTime > self.__duration:
                alpha = (self.__fade - self._elapsedTime) * 255
                
            
            # Outline
            self._text.color = sf.Color(0, 0, 0, alpha);
            self._text.position = ( self._text.position.x - 2, self._text.position.y - 2 )
            window.draw(self._text)
            self._text.position = ( self._text.position.x + 2, self._text.position.y + 2 )
            
            self._text.color = sf.Color(255, 0, 0, alpha);
            window.draw(self._text)
       
    def handleEvent(self, event, mousepos, GUI):
        return
        
# Global object
Errorshower = errorshower(530, 480)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
