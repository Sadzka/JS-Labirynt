from sfml import sf

class GUIManager:
    
    def __init__(self, window):
        self._window = window
        self._widgets = []
    
    def addWidget(self, widget):
        self._widgets.append(widget)
        
    def draw(self, window):
        for widget in self._widgets:
            widget.draw(self._window)
            
    def handleEvent(self, event):
        for widget in self._widgets:
            widget.handleEvent(event, self._window, self)
    
    def focusMe(self, widget):
        for w in self._widgets:
            if widget == w:
                w.setFocus(True)
                #print("Set T : ", w, w.isFocused(), w.getText())
            else:
                w.setFocus(False)
                #print("Set F : ", w, w.isFocused(), w.getText())
            
            
            #print(w, w.isFocused(), w.getText())