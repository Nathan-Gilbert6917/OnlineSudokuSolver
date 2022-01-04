#@Author Mohammed Arab Edits by Nathan Gilbert

# Takes in the board and returns true if the board is valid (no repeat in values in cols, rows + area) or false if invalid
def check_board(board):
    # Checks for duplicate values in each area, if duplicate values exist, return false
    for area in range(1,10):
        area_values = board.gather_filled_values_area(area)
        area_values.sort()
        nums = [1,2,3,4,5,6,7,8,9]
        if nums != area_values:
            return False

    # Checks for duplicate values in each col + row, if duplicate values exist, return false
    for cell in board.board_layout:
        # Check for each column
        valid_columns = check_board_line(cell, board, 'col')
        if not valid_columns:
            return False
        # Check for each row
        valid_rows = check_board_line(cell, board, 'row')
        if not valid_rows:
            return False
    return True

def check_board_line(cell, board, line_direction):
    board_line = board.gather_filled_values_full_line(cell, line_direction)
    line_counter = 0
    for cell_in_line in board_line:
        if cell_in_line == cell.value:
            line_counter += 1
    return line_counter == 1

