from sfml import sf

from GUI.widget import Widget

class Image(Widget):
    """Widget to display images."""
    def __init__(self, texture, x=0, y=0):
        """
        Create a Image object
        
        Parameters:
            texture (sf.Texture) : texture to show on image
            x (int) : position of left corner
            y (int) : position of upper corner
        """
        super().__init__(x, y)
        
        filename = 'img/' + texture + '.png'
        
        try:
            texture = sf.Texture.from_file(filename)
        except IOError as error:
            print("An error occured: {0}".format(error))
            exit(1)
        
        self.sprite = sf.Sprite(texture)
        attributes = [attr for attr in dir(self.sprite)]
        self.selfupdate()
          
    def draw(self, window):
        """
        Draw this widget in window.
        
        Parameters:
            window (Window) : Window to draw.
        """
        window.draw(self.sprite)
        
    def selfupdate(self):
        self.sprite.position = self._position
        self.sprite.ratio = ( (self._size[0]/32, self._size[1]/32) )