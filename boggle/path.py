import numpy as np

class Path:
    
    def __init__(self, nodes: np.array, gridsize: tuple):
        self.nodes = nodes
        self.gridsize = gridsize
        
    def find_neighbours(self):
        options = np.array([[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]])
        new_options = np.tile(self.nodes[-1],[8,1]) + options
        within_x_bounds = np.logical_and(new_options[:,0]>=0, new_options[:,0]<self.gridsize[0])
        within_y_bounds = np.logical_and(new_options[:,1]>=0, new_options[:,1]<self.gridsize[1])
        already_visited = np.apply_along_axis(lambda x: self.is_row_in_array(x,self.nodes),arr=new_options,axis=1)
        return new_options[np.logical_and(np.logical_and(within_x_bounds,within_y_bounds),~already_visited)]
    
    def get_new_paths(self):
        return [Path(nodes=np.vstack((self.nodes, neighbour)), gridsize=self.gridsize) for neighbour in self.find_neighbours()]
    
    def grid_to_text(self, boggle_grid: np.array):
        return ''.join(boggle_grid[self.nodes[:,0],self.nodes[:,1]].tolist())
    
    @staticmethod 
    def is_row_in_array(row , arr):
        return (arr == row).all(axis=1).any()
    
    def __str__(self):
        return str(f'Path in {self.gridsize} grid: {self.nodes.tolist()}')
    
    def __repr__(self):
        return str(f'Path in {self.gridsize} grid: {self.nodes.tolist()}')