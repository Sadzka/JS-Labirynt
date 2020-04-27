from sfml import sf
from widget import Widget

class Image(Widget):

    def __init__(self, texture, x=0, y=0):
        
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
        window.draw(self.sprite)
        
    def selfupdate(self):
        self.sprite.position = self.position
        self.sprite.ratio = ( (self._size[0]/32, self._size[1]/32) )
        
        #print( self.sprite.ratio )
        #print( self.sprite.ratio )
        #print( self.sprite.__name__ )
        #self.sprite.scale( (self.i, self.i) )