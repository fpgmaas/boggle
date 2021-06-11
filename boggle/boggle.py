import numpy as np
from typing import List
from boggle.bisect import HasPrefix, AdaptPrefix, Prefix
from boggle.path import Path
from boggle.boggle_grid import BoggleGrid
import bisect

class Boggle:
    
    def __init__(self, boggle_grid: BoggleGrid, word_list: np.array):
        """
        if boggle_grid = None, create random
        """
        self.boggle_grid = boggle_grid
        self.word_list = word_list
        self.word_list_searchable = AdaptPrefix(word_list)
        
    def solve(self):
        paths = self.initialize_paths()
        all_words = []
        all_words_found = False
        while not all_words_found:
            paths = [y for x in [path.get_new_paths() for path in paths] for y in x]
            idx_to_keep = []
            for idx, path in enumerate(paths):
                word = self.path_to_text(path)
                words_with_prefix = self.get_words_with_prefix(word)
                if len(words_with_prefix)>0:
                    # check if the current path is a word.
                    if word in words_with_prefix:
                        all_words.append({'word': word, 'path': path.nodes})
                        if len(words_with_prefix)>1:
                            idx_to_keep.append(idx)
                    else:
                        idx_to_keep.append(idx)
            paths = [paths[i] for i in idx_to_keep]
            if len(idx_to_keep) == 0:
                all_words_found=True
        return all_words
         
    def initialize_paths(self) -> List[Path]:
        """
        Initialize a Path of length 1 at every point in the grid.
        """
        starting_coords = [np.array([[x,y]]) for x in range(self.boggle_grid.get_gridsize()[0]) for y in range(self.boggle_grid.get_gridsize()[1])]
        return [Path(nodes = xy,gridsize=self.boggle_grid.get_gridsize()) for xy in starting_coords]
    
    def get_words_with_prefix(self, prefix):
        left_index = bisect.bisect_left(self.word_list_searchable, Prefix(prefix))
        right_index = bisect.bisect_right(self.word_list_searchable, Prefix(prefix))
        return self.word_list[left_index:right_index]
            
    def path_to_text(self, path: Path):
        return ''.join(self.boggle_grid.get_grid()[path.nodes[:,0],path.nodes[:,1]].tolist())