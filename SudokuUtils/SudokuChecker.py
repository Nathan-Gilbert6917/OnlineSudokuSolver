#Takes in the board and returns true or false if valid
import SudokuBuilder as builder

def sudokuChecker(board):
    for cell in board.board_layout:
        row = []
        if (board.board_layout.index(cell) < 8):
            row = board.board_layout[0:9]
        elif (board.board_layout.index(cell) < 17):
            row = board.board_layout[9:18]
        elif (board.board_layout.index(cell) < 26):
            row = board.board_layout[18:27]
        elif (board.board_layout.index(cell) < 35):
            row = board.board_layout[27:36]
        elif (board.board_layout.index(cell) < 44):
            row = board.board_layout[36:45]
        elif (board.board_layout.index(cell) < 53):
            row = board.board_layout[45:54]
        elif (board.board_layout.index(cell) < 62):
            row = board.board_layout[54:63]
        elif (board.board_layout.index(cell) < 71):
            row = board.board_layout[63:72]
        elif (board.board_layout.index(cell) < 80):
            row = board.board_layout[72:81]
        
        for cell1 in row:
            counter = 0
            if cell1 == cell:
                counter += 1
        if counter >= 2:
            print("invalid: index " + str(board.board_layout.index(cell)) + "(which is equal to "+ str(cell.value) + ") on the board is equal to index " + str(row.index(cell1)) + 
            "(which is equal to " + str(cell1.value) +")in the row")
            return False
        else:
            print("Wonderful, no repeated values for the boardCell at index " + str(board.board_layout.index(cell)) + " on the Board")
    

board = builder.Board()
print(board)
sudokuChecker(board)

#use gather_filled_values_area and gather_filled_values_full_line in the sudoku builder 


#Can start with 'for each cell in board_layout
#to check the row, you can start by checking the index of the boardCell in your board layout. If index < 8, then make a variable called row = board.boardlayout[0:9]. 
#elif index < 17, then make a variable called row = board.boardlayout[9:18]. elif index < 26, then make a variable called row = board.boardlayound[18-27]
#Now you're creating a list of values that you need to check your boardcell value against. Now I can do: for each cell1 in this new list, 
# if cell1 == cell(value from previous loop), return false

