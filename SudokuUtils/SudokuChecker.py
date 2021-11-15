#@Author Mohammed Arab 

#Takes in the board and returns true if the board is valid (no repeat in values in cols, rows + area) or false if invalid
def sudokuChecker(board):

    #Checks for duplicate values in each area, if duplicate values exist, return false
    for area in range(1,10):
        area_values = board.gather_filled_values_area(area)
        area_values.sort()
        nums = [1,2,3,4,5,6,7,8,9]
        if nums != area_values:
            return False

    #Checks for duplicate values in each col + row, if duplicate values exist, return false
    #Check for each column
    for cell in board.board_layout:
        cell_col = board.gather_filled_values_full_line(cell,'col')
        col_counter = 0
        for cell_in_col in cell_col:
            if cell_in_col == cell:
                col_counter += 1
        if col_counter >= 2:
            return False
        
        #Check for each row
        cell_row = board.gather_filled_values_full_line(cell,'row')
        row_counter = 0
        for cell_in_row in cell_row:
            if cell_in_row == cell:
                row_counter += 1
        if row_counter >= 2:
            return False
    
    return True


