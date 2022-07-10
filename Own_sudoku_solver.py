from pprint import pprint

class sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def find_new_empty(self, puzzle):
        for r in range(9):
            for c in range(9):
                if self.puzzle[r][c] == -1:
                    return r, c

        return None, None

    def is_valid(self, puzzle, guess, row, col):
        #i have to check, that row, col and small square has unique numbers (from 1 to 9)

        row_check = self.puzzle[row]
        if guess in row_check:
            return False

        col_check = []
        for i in range(9):
            col_check.append(self.puzzle[i][col])

        if guess in col_check:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if guess == self.puzzle[r][c]:
                    return False

        return True
    # @staticmethod
    # def board_visualization(cube):
    #     show = []
    #     for r in range(9):
    #         show.append(cube[r])
    #     for r in range(9):
    #         for c in range(9):
    #             if show[r][c] == -1:
    #                 show[r][c] = 0
    #     for i in range(9):
    #         print(show[i])

    def solve_sudoku(self, puzzle):

       row, col = self.find_new_empty(puzzle)

       if row is None:
           return True

       for guess in range(1,10):
           if self.is_valid(puzzle, guess, row, col):
               self.puzzle[row][col] = guess
               if self.solve_sudoku(puzzle):
                   return True

           self.puzzle[row][col] = -1

       return False

if __name__ == "__main__":

    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, 7],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    def board_visualization(cube):
        show = []

        for r in range(9):
            show.append(cube[r])
        for r in range(9):
            for c in range(9):
                if show[r][c] == -1:
                    show[r][c] = 0
        for i in range(9):
            print(show[i])
    board_visualization(example_board)

    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, 7],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]

    Sudoku_solver1 = sudoku(example_board)
    #Sudoku_solver1.board_visualization(example_board)


    print(Sudoku_solver1.solve_sudoku(example_board))
    pprint(Sudoku_solver1.puzzle)
