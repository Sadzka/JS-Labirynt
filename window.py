from sfml import sf

class Window:
    __open = True
    __focused = True
    def __init__(self, wsize):
        width, height = wsize
        self.__window = sf.RenderWindow(sf.VideoMode(width, height), "Konrad Paluch - Labirynt", sf.Style.CLOSE)
        self.__window.vertical_synchronization = True
        self.__window.framerate_limit = 60
    
    def isOpen(self):
        return self.__open
    
    def getRenderWindow(self):
        return self.__window
        
    def isFocused(self):
        return self.__focused
        
    def update(self, gui):
        for event in self.__window.events:
            if event == sf.Event.LOST_FOCUS:
                self.__focused = False
            elif event == sf.Event.GAINED_FOCUS:
                self.__focused = True
            
            if event == sf.Event.CLOSED:
                self.__window.close()
                self.__open = False
                
            gui.handleEvent(event)