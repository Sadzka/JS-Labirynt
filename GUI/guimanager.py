from sfml import sf

class GUIManager:
    """Class to manage GUI Elements."""
    def __init__(self, window, map):
        """
        Create a GUIManager.

        Parameters:
            window (Window) : A window object
            map (Map): A maze object
        """
        self.__window = window
        self.__widgets = []
        self.__map = map
    
    def add_widget(self, widget):
        self.__widgets.append(widget)
    
    def update(self, time):
        """
        Update time in all widget.
        
        Parameters:
            time (float) : time to add to widgets (seconds).
        """
        for widget in self.__widgets:
            widget.update(time)
        
    def draw(self, window):
        """
        Draw this widget in window.
        
        Parameters:
            window (Window) : Window to draw.
        """
        for widget in self.__widgets:
            widget.draw(self.__window)
            
    def handle_event(self, event):
        """
        Handle window event.
        
        Parameters:
            event (sf.Event) : Event to handle.
        """
        mousepos = sf.Mouse.get_position(self.__window)
        
        # Return if window is in background
        if not self.__window.has_focus():
            return
            
        for widget in self.__widgets:
            widget.handle_event(event, mousepos, self)
            
        self.__map.handle_event(event, mousepos)
    
    def focus_me(self, widget):
        """
        Focus this widget and defocus rest of widgets.
        
        Parameters:
            widget (Widget) : Widget to focus
        """
        for widg in self.__widgets:
            if widget == widg:
                widg.set_focus(True)
            else:
                widg.set_focus(False)

