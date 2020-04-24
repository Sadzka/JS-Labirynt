from sfml import sf

class Window:
    open = True
    focused = True
    def __init__(self, width, height):
        self.window = sf.RenderWindow(sf.VideoMode(width, height), "Konrad Paluch - Labirynt")
        self.window.vertical_synchronization = True
        self.window.framerate_limit = 60
    
    def isOpen(self):
        return self.open
    
    def getRenderWindow(self):
        return self.window
        
    def update(self, dtime):
    
        for event in self.window.events:
            if event == sf.Event.LOST_FOCUS:
                focused = False
            elif event == sf.Event.GAINED_FOCUS:
                focused = True
            
            if event == sf.Event.CLOSED:
                self.window.close()