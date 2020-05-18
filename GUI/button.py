"""Clickable widget to handle event on click."""
from sfml import sf

from GUI.widget import Widget
from GUI.widget import font
from GUI.text import Text


MOUSE_LEFT, MOUSE_RIGHT, MOUSE_MIDDLE = range(3)

class Button(Text):

    def __init__(self, x=0, y=0, text="Button"):
        """
        Create a Button object.
        Parameters:
        x (int) : position of left corner
        y (int) : position of upper corner
        text (str) : text in button
        """
        super().__init__(text, x, y)
        self.__left_callback = 0
        self.__right_callback = 0
        
    def selfupdate(self):
        """
        Update required variables.
        """
        self._text.position = self._position
        
    def bind_left_callback(self, funct):
        """
        Set function to call on left mouse click.
        Parameters:
        funct (function) : function to call on left mouse click
        """
        self.__left_callback = funct
        
    def bind_right_callback(self, funct):
        """
        Set function to call on right mouse click.
        Parameters:
        funct (function) : function to call on right mouse click
        """
        self.__left_callback = funct
    
    def handle_event(self, event, mousepos, GUI):
        """
        Handle window event.
        
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
                GUI.focus_me(self)
                if event['button'] ==  MOUSE_LEFT:
                    if self.__left_callback != 0:
                        self.__left_callback()   
                elif event['button'] ==  MOUSE_RIGHT:
                    if self.__right_callback != 0:
                        self.__right_callback()