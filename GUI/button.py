from sfml import sf
from GUI.widget import Widget
from GUI.widget import font
from GUI.text import Text

class Button(Text):

    def __init__(self, x=0, y=0, text="Button"):
        """
        Create a Button object
        Parameters:
        x (int) : position of left corner
        y (int) : position of upper corner
        text (str) : text in button
        """
        super().__init__(text, x, y)
        __leftCallback = 0
        __rightCallback = 0
        
    def selfupdate(self):
        """
        Update required variables
        """
        self._text.position = self._position
        
    def bindLeftCallback(self, funct):
        """
        Set function to call on left mouse click
        Parameters:
        funct (function) : function to call on left mouse click
        """
        self.__leftCallback = funct
        
    def bindRightCallback(self, funct):
        """
        Set function to call on right mouse click
        Parameters:
        funct (function) : function to call on right mouse click
        """
        self.__leftCallback = funct
    
    def handleEvent(self, event, mousepos, GUI):
        """
        Handle window event
        
        Parameters:
        event (sf.Event) : Event to handle.
        mousepos (int, int) : Position of mouse.
        GUI (GUIManager) : GUIManager with widgets.
        """
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