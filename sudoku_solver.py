class SudokuSolver:
    def __init__(self, size: int = 9, start_grid: list = None):
        self.size = size
        self.board = Board(size=self.size, grid=start_grid)
        self.solved = False

    def validate(self, i, j, to_check):
        is_row_valid = all([to_check != self.board.grid[i][x] for x in range(self.size)])
        if is_row_valid:
            is_column_valid = all([to_check != self.board.grid[x][j] for x in range(self.size)])
            if is_column_valid:
                square_x, square_y = 3 * (i // 3), 3 * (j // 3)
                for x in range(square_x, square_x + 3):
                    for y in range(square_y, square_y + 3):
                        if self.board.grid[x][y] == to_check:
                            return False
                return True
        return False

    def solve(self):
        self.solved = self.__solve()
        self.board.print_grid()
        return self.board.grid

    def __solve(self, i=0, j=0):
        i, j = self.board.next_field(i, j)
        if i == -1:
            return True
        for e in range(1, 10):
            if self.validate(i, j, e):
                self.board.grid[i][j] = e
                if self.__solve(i, j):
                    return True
                self.board.grid[i][j] = 0
        return False


class Board:
    def __init__(self, size: int = 9, grid: list = None):
        self.size = size
        self.grid = grid
        if not self.grid:
            self.grid = [[0 for x in range(self.size)] for y in range(self.size)]

    def print_grid(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.grid[x][y], end=" ")
            print()

    def next_field(self, i: int, j: int):
        for x in range(i, self.size):
            for y in range(j, self.size):
                if self.grid[x][y] == 0:
                    return x, y
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.grid[x][y] == 0:
                    return x, y
        return -1, -1
