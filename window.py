from sfml import sf

class Window:
    """
    The class to manage window.
    """

    __open = True
    def __init__(self, wsize):
        """
        Create a window.

        Parameters:
            wsize (int, int): x and y size of window
        """
        
        width, height = wsize
        self.__window = sf.RenderWindow(sf.VideoMode(width, height), "Konrad Paluch - Labirynt", sf.Style.CLOSE)
        self.__window.vertical_synchronization = True
        self.__window.framerate_limit = 60
    
    def is_open(self):
        return self.__open
    
    def get_render_window(self):
        return self.__window
        
    def update(self, gui):
        """
        Update window and handle event.

        Parameters:
            GUIManager : GUIManager to update
        """
        for event in self.__window.events:
            
            if event == sf.Event.CLOSED:
                self.__window.close()
                self.__open = False
                
            gui.handle_event(event)