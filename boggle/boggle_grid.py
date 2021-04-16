import numpy as np
from typing import List

class BoggleGrid:
    
    def __init__(self, boggle_grid: np.array = None, letter_probs: dict = None, gridsize: tuple = None):
        """
        if boggle_grid = None, create random
        """
        if boggle_grid:
            self.boggle_grid = boggle_grid
            self.gridsize = boggle_grid.shape
        else:
            self.boggle_grid = self.create_random_grid(letter_probs, gridsize)
            self.gridsize = gridsize
            
    @staticmethod
    def create_random_grid(letter_probs, gridsize):
        return np.random.choice(list(letter_probs.keys()), size=gridsize, replace=False, p=list(letter_probs.values())) 
    
    def print_as_upper(self):
        return str(np.matrix(np.char.upper(self.boggle_grid)))

    def get_grid(self):
        return self.boggle_grid

    def get_gridsize(self):
        return self.gridsize
    
    def __str__(self):
        return str(np.matrix(self.boggle_grid))
    
    def __repr__(self):
        return str(np.matrix(self.boggle_grid))