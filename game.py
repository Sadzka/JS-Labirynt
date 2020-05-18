from sfml import sf
import GUI
from GUI.errorshower import Errorshower as ES
from window import Window
from map import Map

class Game:
    """
    The class that stores the window, draws and updates it
    """
    __windowsize = (1060, 960)
    __window = Window(__windowsize)
    __clock = sf.Clock()
    __map = Map(__windowsize)
    
    __GuiManager = GUI.guimanager.GUIManager(__window.get_render_window(), __map)
    
    def __init__(self):
        self.__load_widgets()
    
    def is_running(self):
        return self.__window.is_open()
    
    def get_window(self):
        return self.__window
        
    def update(self):
        dtime = self.__clock.restart().seconds
        
        self.__window.update(self.__GuiManager)
        self.__GuiManager.update(dtime)
        
    def render(self):
        """
        Draw all objects in window.
        """
        sizex, sizey = self.__map.get_size()
        tilex, tiley = self.__map.get_tiles_size()
        
        self.wall.set_size(tilex, tiley)
        self.way.set_size(tilex, tiley)
        self.start.set_size(tilex, tiley)
        self.end.set_size(tilex, tiley)
        self.indirect.set_size(tilex, tiley)
        self.userindirect.set_size(tilex, tiley)
        
        map = self.__map.get_map()
 
        wind = self.__window.get_render_window()
        
        # clear the window
        wind.clear( sf.Color(0, 0, 0) )
        
        # draw content
        if tilex != 0 or tiley != 0:
            for i in range(sizex):
                for j in range(sizey):
                    if map[i][j] == 0:
                        self.wall.set_position(i*tilex, j*tiley)
                        self.wall.draw(wind)
                    elif map[i][j] == 1:
                        self.way.set_position(i*tilex, j*tiley)
                        self.way.draw(wind)
                    elif map[i][j] == 2:
                        self.start.set_position(i*tilex, j*tiley)
                        self.start.draw(wind)
                    elif map[i][j] == 3:
                        self.end.set_position(i*tilex, j*tiley)
                        self.end.draw(wind)
                    elif map[i][j] == 4:
                        self.indirect.set_position(i*tilex, j*tiley)
                        self.indirect.draw(wind)
                    elif map[i][j] == 5:
                        self.userindirect.set_position(i*tilex, j*tiley)
                        self.userindirect.draw(wind)
        
        self.__GuiManager.draw(wind)
        
        # display window
        wind.display()
    
    def __load_widgets(self):
        """
        Load widgets.
        """
        self.wall = GUI.image.Image("wall")
        self.way = GUI.image.Image("way")
        self.start = GUI.image.Image("start")
        self.end = GUI.image.Image("end")
        self.indirect = GUI.image.Image("indirect")
        self.userindirect = GUI.image.Image("userindirect")
        
        edit_box_x = GUI.editbox.EditBox(sizex=96, sizey=28, text="30")
        edit_box_x.set_position(960, 16)
        
        edit_box_y = GUI.editbox.EditBox(sizex=96, sizey=28, text="30")
        edit_box_y.set_position(960, 60)
        
        button_showgrid = GUI.button.Button(text="Show Grid")
        button_showgrid.set_position(960, 100)
        button_showgrid.bind_left_callback(lambda: self.__map.generate_grid(edit_box_x.get_text(), edit_box_y.get_text()))
        
        button_generate = GUI.button.Button(text="Generate")
        button_generate.set_position(960, 150)
        button_generate.bind_left_callback(lambda: self.__map.generate())

        button_solve = GUI.button.Button(text="Solve")
        button_solve.set_position(960, 200)
        button_solve.bind_left_callback(lambda: self.__map.solve_maze())
        
        button_clear_solve = GUI.button.Button(text="Clear Solve")
        button_clear_solve.set_position(960, 250)
        button_clear_solve.bind_left_callback(lambda: self.__map.clear_solve())
        button_clear_solve.set_character_size(18)
        
        button_clear_points = GUI.button.Button(text="Clear points")
        button_clear_points.set_position(960, 300)
        button_clear_points.bind_left_callback(lambda: self.__map.clear_points())
        button_clear_points.set_character_size(18)
        
        self.__GuiManager.add_widget(edit_box_x)
        self.__GuiManager.add_widget(edit_box_y)
        self.__GuiManager.add_widget(button_showgrid)
        self.__GuiManager.add_widget(button_generate)
        self.__GuiManager.add_widget(button_solve)
        self.__GuiManager.add_widget(button_clear_solve)
        self.__GuiManager.add_widget(button_clear_points)
        self.__GuiManager.add_widget(ES)