from sfml import sf

class GUIManager:
    
    def __init__(self, window, map):
        self.__window = window
        self.__widgets = []
        self.__map = map
    
    def addWidget(self, widget):
        self.__widgets.append(widget)
    
    def update(self, time):
        for widget in self.__widgets:
            widget.update(time)
        
    def draw(self, window):
        for widget in self.__widgets:
            widget.draw(self.__window)
            
    def handleEvent(self, event):
        mousepos = sf.Mouse.get_position(self.__window)
        
        for widget in self.__widgets:
            widget.handleEvent(event, mousepos, self)
            
        self.__map.handleEvent(event, mousepos)
    
    def focusMe(self, widget):
        for w in self.__widgets:
            if widget == w:
                w.setFocus(True)
            else:
                w.setFocus(False)