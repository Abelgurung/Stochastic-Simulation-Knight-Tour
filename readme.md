## Stochastic Simulation for Solving Knight's Tour Problem

<p align="center">
    <img src="/path_tracing.gif" alt="Path Tracing Animation" height="500"> 
</p>

The Knight's Tour is a classic problem in the field of chess and mathematics, particularly in graph theory. It involves moving a knight on a chessboard in such a way that it visits every square exactly once. If the knight ends on a square that is one knight's move from the beginning square (thus, it could continue with the same path), the tour is closed; otherwise, it is open.

The chessboard can be of any size, but the problem is traditionally considered on the standard 8x8 board. The knight moves in an L-shape. This unique movement creates a complex challenge in arranging a tour that covers all 64 squares without repetition.

Mathematically, the Knight's Tour can be represented as a Hamiltonian path or cycle (for closed tours) in a graph constructed from the chessboard, where each square is a node and each legal knight move is an edge. Finding a Knight's Tour is a specific instance of the more general Hamiltonian path problem, which is NP-complete for arbitrary graphs but solvable for the specific structure of the knight's movements on a chessboard.

The purpose of this program is not to search efficiently; instead, it is to do more statistical studies on the complex patterns made by stochastic processes.

This Python class, named `mc_search`, implements a Monte Carlo search method to generate a path for a knight on a chessboard, given a starting position and board size. The class is specifically designed to simulate the knight's legal moves across the chessboard to explore different positions without revisiting the same spot. Here's a detailed breakdown of its components and functionality:

### Initialization

Let $N$ be the size of the chessboard, which is an $N \times N$ grid. Let $s = (x_s, y_s)$ be the starting position of the knight on the board, where $x_s$ and $y_s$ are the coordinates on the chessboard.

The Monte Carlo search for a knight's tour is initialized with:

- The chessboard size $N$.
- The current position $c = s$, initially set to the starting position.
- The path $P$ of visited positions, initially $P = \lbrace s \rbrace$.
- The set of knight moves $M$, where $M = \lbrace(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)\rbrace$.

## Process

Start with the current position $c = s$ and an initial path $P = \lbrace s \rbrace$.

### Search

For each step $i$ from $1$ to $k$, where $k$ is the maximum number of steps:

#### a. Generate Potential Moves

For the current position $c = (x_c, y_c)$, calculate potential moves $P_M = \lbrace c + m | m \in M \rbrace$.

#### b. Validate Moves

- Filter out moves that go outside the chessboard bounds to get $P_M' = \lbrace m \in P_M | 0 \leq m_x < N \land 0 \leq m_y < N \rbrace$, where $m = (m_x, m_y)$.
- Further filter $P_M'$ to exclude moves leading to previously visited positions, resulting in the set of valid moves $V = \lbrace m \in P_M' | m \notin P \rbrace$.

#### c. Select and Move

- If $V$ is empty, the search terminates as no further moves are possible.
- Otherwise, randomly select a new position $c'$ from $V$, set $c = c'$, and append $c'$ to $P$.

### Termination

The search concludes when either no valid moves are available or the maximum number of steps $k$ is reached. The output is the path $P$, representing the sequence of moves made from the starting position.

### Class Definition: `mc_search`

- **Purpose**: To simulate and track the movement of a knight on a chessboard, ensuring it only makes legal moves according to the rules of chess and does not revisit any position.
- **Parameters**:
  - `board_size`: An integer representing the dimensions of the square chessboard (e.g., 8 for an 8x8 board).
  - `start`: A tuple or list specifying the knight's starting position on the board in the form `(row, column)`.

### Attributes

- `board_size`: Stores the size of the chessboard.
- `curr`: A NumPy array representing the current position of the knight on the chessboard.
- `path`: A list of tuples, where each tuple represents a position (as `(row, column)`) visited by the knight on the chessboard.
- `knight_moves`: A NumPy array containing the relative moves a knight can make from any position, encoded as row and column offsets.

### Methods

- **`valid_positions(self, curr)`**:

  - **Purpose**: To calculate all legal moves the knight can make from its current position that are within the bounds of the chessboard and have not been previously visited.
  - **Parameters**:
    - `curr`: The current position of the knight as a NumPy array.
  - **Returns**: A list of possible moves the knight can make next, filtered to ensure they are within the chessboard's boundaries and are not revisiting any previously visited positions.

- **`run(self, steps=64)`**:
  - **Purpose**: To execute the Monte Carlo search, moving the knight across the chessboard for a specified number of steps or until no more legal moves are available.
  - **Parameters**:
    - `steps`: An optional integer specifying the number of moves to simulate. Defaults to 64, which is the total number of squares on a standard 8x8 chessboard.
  - **Returns**: A NumPy array containing the path of the knight's movement across the chessboard. Each element in the array is a tuple representing a position visited by the knight.

### Functionality

- The class begins with initializing the chessboard size, the knight's starting position, and the possible knight moves.
- It keeps track of all positions visited by the knight to prevent revisiting.
- The `valid_positions` method dynamically calculates legal moves from the current position considering the chessboard's boundaries and previously visited spots.
- The `run` method iterates through a specified number of steps or until no legal moves remain, randomly selecting from the available legal moves at each step to simulate the knight's path.
- This Monte Carlo method allows for the exploration of the knight's movement patterns on the chessboard, useful for studying the knight's tour problem or for creating educational tools and simulations.
