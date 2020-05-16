from sfml import sf

class Window:
    __open = True
    __focused = True
    def __init__(self, wsize):
        """
        Create a window

        Parameters:
        wsize (int, int): x and y size of window
        """
        
        width, height = wsize
        self.__window = sf.RenderWindow(sf.VideoMode(width, height), "Konrad Paluch - Labirynt", sf.Style.CLOSE)
        self.__window.vertical_synchronization = True
        self.__window.framerate_limit = 60
    
    def isOpen(self):
        """
        Create a window

        Returns:
        bool: Is window open?
        """
        return self.__open
    
    def getRenderWindow(self):
        """
        Return a RenderWindow for drawing

        Returns:
        sf.RenderWindow: Window to drawing
        """
        return self.__window
        
    def isFocused(self):
        """
        Return a boolean value - is the window focused

        Returns:
        bool: Is window focused?
        """
        return self.__focused
        
    def update(self, gui):
        """
        Update window and handle event

        Parameters:
        GUIManager : GUIManager to update
        """
        for event in self.__window.events:
            if event == sf.Event.LOST_FOCUS:
                self.__focused = False
            elif event == sf.Event.GAINED_FOCUS:
                self.__focused = True
            
            if event == sf.Event.CLOSED:
                self.__window.close()
                self.__open = False
                
            gui.handleEvent(event)