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
        self.update()
        
        
    def draw(self, window):
        window.draw(self.sprite)
        
    def update(self):
        self.sprite.position = self.position
        #self.sprite.resize( (self.size[0]/32 * 1.1, self.size[1]/32 * 1.1) )