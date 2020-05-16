from sfml import sf

class GUIManager:
    
    def __init__(self, window, map):
        """
        Create a GUIManager

        Parameters:
        window (Window) : A window object
        map (Map): A maze object
        """
        self.__window = window
        self.__widgets = []
        self.__map = map
    
    def addWidget(self, widget):
        """
        Add widget to manager
        Parameters:
        widget (Widget) : Widget to add.
        """
        self.__widgets.append(widget)
    
    def update(self, time):
        """
        Update time in all widget
        Parameters:
        time (float) : time to add to widgets (seconds).
        """
        for widget in self.__widgets:
            widget.update(time)
        
    def draw(self, window):
        """
        Draw this widget in window
        Parameters:
        window (Window) : Window to draw.
        """
        for widget in self.__widgets:
            widget.draw(self.__window)
            
    def handleEvent(self, event):
        """
        Handle window event
        
        Parameters:
        event (sf.Event) : Event to handle.
        """
        mousepos = sf.Mouse.get_position(self.__window)
        
        for widget in self.__widgets:
            widget.handleEvent(event, mousepos, self)
            
        self.__map.handleEvent(event, mousepos)
    
    def focusMe(self, widget):
        """
        Focus this widget and defocus rest of widgets
        
        Parameters:
        widget (Widget) : Widget to focus
        """
        for w in self.__widgets:
            if widget == w:
                w.setFocus(True)
            else:
                w.setFocus(False)