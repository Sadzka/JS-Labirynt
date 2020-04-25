from sfml import sf

class GUIManager:
    widgets = []
    
    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def draw(self, window):
        for widget in self.widgets:
            widget.draw(window)