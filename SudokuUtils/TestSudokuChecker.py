import unittest
import SudokuBuilder as builder
import SudokuChecker as checker     #if this doesnt work, try 'from'

#edit as needed
class TestSudokuBuilder(unittest.TestCase):
  def test_generate_board(self):
    board = builder.Board()
    count = 0
    for cell in board.board_layout:
      if cell.value == 0:
        count += 1
    self.assertTrue(count == 0)



if __name__ == '__main__':
  unittest.main()