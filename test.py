import pytest

from sudoku_solver import SudokuSolver, Board


class TestBoard:
    @pytest.mark.parametrize("test_size", [0, 1, 5, 9, 10, 999])
    def test_board_size(self, test_size):
        b = Board(size=test_size)
        assert len(b.grid) == test_size
        for row in b.grid:
            assert len(row) == test_size

    @pytest.mark.parametrize("x, y, next_x, next_y", [
        (0, 0, 0, 1),
        (1, 1, 1, 2),
        (8, 8, 0, 0),
    ])
    def test_next_field(self, x, y, next_x, next_y):
        b = Board(size=9)
        b.grid[x][y] = 1
        next_field = b.next_field(x, y)
        assert next_field == (next_x, next_y)
