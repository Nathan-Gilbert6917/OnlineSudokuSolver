import unittest
import SudokuBuilder as builder
import SudokuChecker as checker     #if this doesnt work, try 'from'

#edit as needed
class TestSudokuChecker(unittest.TestCase):
  def test_generate_board(self):
    board = builder.Board()
    self.assertTrue(checker.check_board(board))



if __name__ == '__main__':
  unittest.main()