from sfml import sf

class GUIManager:
    widgets = []
    
    def __init__(self, window):
        self.window = window
    
    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def draw(self, window):
        for widget in self.widgets:
            widget.draw(window)
            
    def handleEvent(self, event):
        for widget in self.widgets:
            widget.handleEvent(event, self.window)