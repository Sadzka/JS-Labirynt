from sfml import sf
import math
import random

window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML - Pong")
window.vertical_synchronization = True
window.framerate_limit = 60
running = True

clock = sf.Clock()

while running:

    delta_time = clock.restart().seconds
    
    # handle events
    for event in window.events:
        if event == sf.Event.CLOSED:
            window.close()

    window.clear(sf.Color.BLACK)
    
    window.display()
    
    
window.close()
