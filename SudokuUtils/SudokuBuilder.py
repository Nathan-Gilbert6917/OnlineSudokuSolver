import random
# File used to generate a random valid sudoku board

# Class to generate a valid sudoku board
class Board():
    def __init__(self):
        self.valid = False
        self.board_layout = []
        # Adds 81 Basic BoardCells to the board 
        for area in range(1,10):
            for area_cell in range(9):
                self.board_layout.append(BoardCell(area))
        # Sets the adjacent cells for each BoardCell
        self._set_adjacent_cells()

        # Fills the whole board with values to see if it is a valid sudoku board
        self.valid = self._fill_board()
        
        # When the board in not valid a new board is created
        # This guarantees that a valid board will be created
        while not self.valid:
            board = Board()
            self.valid = board.valid
            if self.valid == True:
                # Sets the board to the generated valid board
                self.board_layout = board.board_layout

    # toString method for testing and displaying the board
    def __str__(self):
        rows = []
        count = 0
        row = []

        # Loops through all cells and adds their value to a row
        for cell in self.board_layout:
            if (count < 9):
                row.append(cell.value)
                count += 1
            else:
                rows.append(row)
                count = 1
                row = []
                row.append(cell.value)
        rows.append(row)
        row_string = ""
        
        # 2D array formatting using the rows of values
        for row in rows:
            for value in row:
                if value >= 0 and value < 10:
                    row_string += " "
                row_string += str(value) + " "
            row_string += '\n'
        return row_string

    # Method to empty a defined number of random cells
    def remove_random_values(self, prefilled):
        empty_cells = 81 - prefilled 
        indexes_used = []
        # Loops x many times where x is the amount of cell to empty
        for x in range(empty_cells):
            self._remove_random_value(empty_cells, indexes_used)

    # Method to empty a single random cell
    def _remove_random_value(self, empty_cells, indexes_used):
        random_cell_index = random.randint(0, 80)
        if random_cell_index not in indexes_used:
            indexes_used.append(random_cell_index)
            self.board_layout[random_cell_index].value = 0
        else:
            self._remove_random_value(empty_cells, indexes_used)

    # Method to fill board of cells with valid areas with valid values
    # Area Layout
    # 1 2 3
    # 4 5 6
    # 7 8 9
    def _fill_board(self):
        count = 0
        # Generates each area starting from the top left to bottom right
        for area in range(9):
            invalid = True
            # Loops until the area is valid or after 200 invalid attempts 
            while invalid:
                invalid = self._generate_valid_area(area + 1)
                count += 1
                if count == 200:
                    return False
            count = 0
        return True

    # Method to fill a designated area of cells with valid values
    def _generate_valid_area(self, area_num):
        for cell in self.board_layout:
            # Generates valid value for cell in the designated area
            if cell.area == area_num:
                value = self._generate_valid_value(cell)
                if value == 0:
                    for cell in self.board_layout:
                        if cell.area == area_num:
                            cell.value = 0
                    return True
        return False
                    
    # Generates a valid value inside an area
    def _generate_valid_value(self, cell):
        # Gathers all values filled in area, row and column of the current cell location 
        area_values_filled = self.gather_filled_values_area(cell.area)
        row_values_filled = self.gather_filled_values_full_line(cell, 'row')
        col_values_filled = self.gather_filled_values_full_line(cell, 'col')
        all_values = area_values_filled + row_values_filled + col_values_filled
        area = [1,2,3,4,5,6,7,8,9]

        # Loops over values in collected filled values to check if they are inside the area list
        # This leaves the values that can be used to randomly choose from to set the cell's value
        for value in all_values:
            if value in area:
                area.remove(value)
        if len(area) != 0:
            cell.value = random.choice(area)
        return cell.value

    # Gathers all the values in a designated area
    def gather_filled_values_area(self, area_num):
        filled_values = []
        for cell in self.board_layout:
            if (cell.area == area_num):
                filled_values.append(cell.value)
        return filled_values

    # Gathers all the values in a row or column of a cell location
    def gather_filled_values_full_line(self, cell, line_type):
        filled_values = []
        filled_values.append(cell.value)
        direction_map = {
            'col': ['top', 'bottom'],
            'row': ['left', 'right']
        }

        directions = direction_map.get(line_type)
        filled_values += self.gather_filled_values_one_direction_line(cell, directions[0])
        filled_values += self.gather_filled_values_one_direction_line(cell, directions[1])
        return filled_values
    
    # Gather values in a row or column of a cell location in a direction
    def gather_filled_values_one_direction_line(self, cell, direction):
        filled_values = []
        current_cell = cell
        while current_cell.get_adjacent_cell(direction) != None:
            current_cell = current_cell.get_adjacent_cell(direction)
            filled_values.append(current_cell.value)
        return filled_values

    # Sets up the adjacent cells of all cells in the board
    def _set_adjacent_cells(self):
        cell_idx = 0
        for cell in self.board_layout:
            if (cell_idx - 1 >= 0 and cell_idx - 1 < 81 and cell_idx % 9 != 0):
                cell.set_adjacent_cell('left', self.board_layout[cell_idx - 1])
            if (cell_idx + 1 >= 0 and cell_idx + 1 < 81 and (cell_idx + 1) % 9 != 0):
                cell.set_adjacent_cell('right', self.board_layout[cell_idx + 1])
            if (cell_idx - 9 >= 0 and cell_idx - 3 < 81):
                cell.set_adjacent_cell('top', self.board_layout[cell_idx - 9])
            if (cell_idx + 9 >= 0 and cell_idx + 9 < 81):
                cell.set_adjacent_cell('bottom', self.board_layout[cell_idx + 9])
            cell_idx += 1



# Class to represent a cell on the board
class BoardCell():
    def __init__(self, area):
        self.value = 0
        self.area = area
        self.adjacent_cells = {
            'left': None,
            'right': None,
            'top': None,
            'bottom': None
        }

    # toString method to display cell value
    def __str__(self):
        return str(self.value)

    # Gathers the adjacent cell in a given position: 'top', 'left', 'right', 'bottom' 
    def get_adjacent_cell(self, position):
        return self.adjacent_cells.get(position.lower(), "Invalid position")

    # Sets the adjacent cell in a given position: 'top', 'left', 'right', 'bottom'
    def set_adjacent_cell(self, position, cell):
        self.adjacent_cells[position.lower()] = cell
