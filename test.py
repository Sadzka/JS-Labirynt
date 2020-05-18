import unittest
from map import Map
from GUI.errorshower import ErrorshowerException

class Test(unittest.TestCase):
    window_size = (1060, 960)
    
    def test_start_end_opposite(self): # Test 1
        maze = Map(self.window_size)
        
        maze.generate_grid(10, 12)
        maze.set_start(0, 0)
        maze.set_end(9, 11)
        self.assertTrue(ErrorshowerException, maze.generate)
        
        
        maze.generate_grid(10, 12)
        maze.set_start(9, 0)
        maze.set_end(0, 11)
        self.assertTrue(ErrorshowerException, maze.generate)
        
    def test_start_end_4range(self): # Test 2
        maze = Map(self.window_size)
        
        maze.generate_grid(20, 10)
        maze.set_start(0, 3)
        maze.set_end(0, 6)
        self.assertTrue(ErrorshowerException, maze.generate)
        
        
        maze.generate_grid(20, 10)
        maze.set_start(10, 6)
        maze.set_end(10, 3)
        self.assertTrue(ErrorshowerException, maze.generate)
        
    def test_start_equal_end(self): # Test 3
        maze = Map(self.window_size)
        maze.generate_grid(10, 10)
        maze.set_start(4, 4)
        maze.set_end(4, 4)
        
        self.assertRaises(ErrorshowerException, maze.generate)
        
    def test_start_end_neighbor(self): # Test 4
        maze = Map(self.window_size)
        maze.generate_grid(10, 10)
        
        maze.set_start(4, 4)
        maze.set_end(5, 4)
        self.assertRaises(ErrorshowerException, maze.generate)
        
        
        maze.set_start(0, 1)
        maze.set_end(0, 2)
        self.assertRaises(ErrorshowerException, maze.generate)
        
        maze.set_start(5, 5)
        maze.set_end(5, 6)
        self.assertRaises(ErrorshowerException, maze.generate)
        
    def test_input_zero_or_less(self): # Test 6
        maze = Map(self.window_size)
        self.assertRaises(ErrorshowerException, maze.generate_grid,  0, 10)
        self.assertRaises(ErrorshowerException, maze.generate_grid, -5, 10)
        self.assertRaises(ErrorshowerException, maze.generate_grid, 10,  0)
        self.assertRaises(ErrorshowerException, maze.generate_grid, 10, -5)
        
    def test_generate_too_large_maze(self): # Test 7
        maze = Map(self.window_size)
        self.assertRaises(ErrorshowerException, maze.generate_grid, 30, 40)
        self.assertRaises(ErrorshowerException, maze.generate_grid, 10, 31)
        self.assertRaises(ErrorshowerException, maze.generate_grid, 3, 64)
        
        
    def test_add_point_in_wall(self): # Test 9
        maze = Map(self.window_size)
        maze.generate_grid(10, 10)
        maze.generate()
        map = maze.get_map()
        
        for x in range(maze.get_size()[0]):
            for y in range(maze.get_size()[1]):
                if map[x][y] == 0:
                    self.assertRaises(ErrorshowerException, maze.add_point, (x, y))
                
if __name__ == "__main__":
    unittest.main() 