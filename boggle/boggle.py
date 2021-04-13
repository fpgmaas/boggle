import numpy as np

class BoggleGrid:
    
    def __init__(self, boggle_grid: np.array = None, letter_probs: dict = None, grid_size: tuple = None):
        """
        if boggle_grid = None, create random
        """
        if boggle_grid:
            self.boggle_grid = boggle_grid
            self.grid_size = boggle_grid.shape
        else:
            self.boggle_grid = self.create_random_grid(letter_probs, grid_size)
            self.grid_size = grid_size
            
    @staticmethod
    def create_random_grid(letter_probs, grid_size):
        return np.random.choice(list(letter_probs.keys()), size=grid_size, replace=False, p=list(letter_probs.values())) 
    
    def print_as_upper(self):
        return str(np.matrix(np.char.upper(self.boggle_grid)))

    def get_grid(self):
        return self.boggle_grid

    def get_grid_size(self):
        return self.grid_size
    
    def __str__(self):
        return str(np.matrix(self.boggle_grid))
    
    def __repr__(self):
        return str(np.matrix(self.boggle_grid))