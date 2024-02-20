import numpy as np
import random

class mc_search:
    def __init__(self, board_size, start):
        self.board_size = board_size
        self.curr = np.array(start)
        self.path = [tuple(self.curr)]
        self.knight_moves = np.array([[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]])
       
    def valid_positions(self, curr):
        possible_moves = self.knight_moves + curr
        mask = np.all((possible_moves >= 0) & (possible_moves < self.board_size), axis=1)
        possible_moves = possible_moves[mask]

        possible_moves = [move for move in possible_moves if tuple(move) not in self.path]
    
        return possible_moves

    def run(self, steps=64):
        for _ in range(steps):
            possible_moves = self.valid_positions(self.curr)

            if len(possible_moves) == 0:
                break
            else:
                self.curr = random.choice(possible_moves)
                self.path.append(tuple(self.curr))
        
        return np.array(self.path)