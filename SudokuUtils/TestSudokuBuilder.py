import unittest
import SudokuBuilder as builder

class TestSudokuBuilder(unittest.TestCase):
  def test_generate_board(self):
    board = builder.Board()
    count = 0
    for cell in board.board_layout:
      if cell.value == 0:
        count += 1
    self.assertTrue(count == 0)


  def test_generate_board_with_values_removed(self):
    for x in range(81):
      board = builder.Board()
      board.remove_random_values(x + 1)
      count = 0
      for cell in board.board_layout:
        if cell.value != 0:
          count += 1
      self.assertTrue(count == x + 1)

if __name__ == '__main__':
  unittest.main()