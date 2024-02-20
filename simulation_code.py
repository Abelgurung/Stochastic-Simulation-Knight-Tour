import numpy as np
import random

class mc_search:
    def __init__(self, board_size, start):
        """
        Initializes the Monte Carlo search for a knight's tour.
        
        Parameters:
        - board_size (int): The size of the chessboard (N x N).
        - start (tuple): The starting position of the knight on the board as a tuple (x, y).
        """
        self.board_size = board_size
        self.curr = np.array(start)
        self.path = [tuple(self.curr)]
        # Defines all possible moves of a knight
        self.knight_moves = np.array([[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]])

    def reset(self, start):
        """
        Reinitializes the Monte Carlo search for a knight's tour for the next iteration.
        Parameters:
        - start (tuple): The starting position of the knight on the board as a tuple (x, y).
        """
        self.curr = np.array(start)
        self.path = [tuple(self.curr)]
        
    def valid_positions(self, curr):
        """
        Determines the valid moves from the current position.
        """
        # Filter out moves that are outside the bounds of the board
        possible_moves = self.knight_moves + curr
        mask = np.all((possible_moves >= 0) & (possible_moves < self.board_size), axis=1)
        possible_moves = possible_moves[mask]

        # Further filter out moves to positions already visited
        possible_moves = [move for move in possible_moves if tuple(move) not in self.path]
    
        return possible_moves

    def run(self, steps=64):
        """
        Runs the Monte Carlo search to find a path for the knight.
        
        Parameters:
        - steps (int): The maximum number of steps (moves) to attempt.
        """
        for _ in range(steps):
            possible_moves = self.valid_positions(self.curr)

            if len(possible_moves) == 0:
                break  
            else:
                self.curr = random.choice(possible_moves)
                self.path.append(tuple(self.curr))
        
        return np.array(self.path)
