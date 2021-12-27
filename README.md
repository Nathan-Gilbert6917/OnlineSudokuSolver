# OnlineSudokuSolver 

There are three main parts to this project:

- React Frontend
- Sudoku Builder
- Sudoku Checker
- Sudoku Solver

The frontend will allow users to interact with a randomly generated Sudoku board

The user can solve the Sudoku themselves by clicking on the board cells and typing a value from 1-9
The user has access to a few buttons:

1st button:
At any point in the puzzle, the user can have the board checked to see if their solution is valid.

2nd button:
The user can generate a new board and start fresh

3rd button:
The user can can use one of their hints to get a cell filled 

4th button:
The user can have the computer solve the Sudoku for them.

# The Sudoku Builder uses a board of cells to represent and generate a valid Sudoku board

The board is generated one cell at a time.
Each cell is connected to each other by setting their adjacent cells.
Then each area on the board is set by setting each cell's corresponding area.
Each cell's value is randomly generated from a list of valid values.
The valid values are determined by checking the values of the cell's area, column and row for validity.
If an area is not valid the area is reset and generated again up to 200 times.
If the 200 time limit is reached the whole board is invalid and a new board is initialized to generate a valid board. This all continues until a valid board is generated and set as the original board's board.

TODO later, fix this by generating a valid board on the first attempt instead of initilizing other boards after 200 attempts per area.

# The Sudoku Checker is a utility function to validate the board state has been validly solved.

# The Sudoku Solver is a utility function to solve the Sudoku board using an algorithm

# Future ideas

- User support
- Friend support
- Global leaderboard score/time/difficulty
- Timed trial against another user
- Timed trial against yourself per difficulty