
import os.path

from game_of_life.cell import Cell


class Board:
    """
        class Board to represent the board in the Game of Life
    """

    def __init__(self, num_rows: int = 0, num_cols: int = 0):
        """
            Creates a new Board with the given rows and cols.
            The board is create empty
        """
        if type(num_rows) is not int or type(num_cols) is not int:
            raise TypeError('num_rows or num_cols not int')

        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__board = []

    def get_num_rows(self) -> int:
        """
            Returns the number of rows of the board
        """
        return self.__num_rows

    def get_num_cols(self) -> int:
        """
            Returns the number of cols of the board
        """
        return self.__num_cols

    def set_num_rows(self, new_rows: int):
        """
            Sets the number of rows of the board with the new value
        """
        if type(new_rows) is not int:
            raise TypeError('num_rows is not int')
        self.__num_rows = new_rows

    def set_num_cols(self, new_cols: int):
        """
            Sets the number of cols of the board with the new value
        """
        if type(new_cols) is not int:
            raise TypeError('num_cols is not int')
        self.__num_cols = new_cols

    def get_board(self) -> list:
        """
            Returns the actual board
        """
        return self.__board

    def __str__(self):
        """
            Returns the string representation of the board
        """
        frame = '#' * (self.__num_cols + 2) + '\n'
        board_str = ''
        for row in self.__board:
            board_str += '#'
            for cell in row:
                board_str += str(cell)
            board_str += '#\n'

        return frame + board_str + frame

    def __check_file_status(self, filename: str):
        """
            Auxiliar method to check the status of the filenames
        """
        if type(filename) is not str:
            raise TypeError('filename is not a string')

        if not os.path.exists(filename):
            raise RuntimeError(f'filename {filename} not exists')

        return True

    def read_from_file(self, filename: str):
        """
            Reads the board from an input file
        """
        if self.__check_file_status(filename):
            with open(filename, 'r') as file_handler:
                lines = file_handler.readlines()
                self.__num_rows = int(lines[0])
                self.__num_cols = int(lines[1])
                for line in lines[2:]:
                    row = []
                    tokens = list(line)[:-1]
                    for token in tokens:
                        cell = None
                        if token == '*':
                            cell = Cell(False)
                        elif token == 'o':
                            cell = Cell(True)
                        else:
                            raise RuntimeError(f'Token {token} not allowed')

                        row.append(cell)
                    self.__board.append(row)

    def write_to_file(self, filename: str):
        """
            Writes the board to an output file
        """
        if self.__check_file_status(filename):
            with open(filename, 'a') as file_handler:
                file_handler.write(str(self))

    def __check_limits(self, row: int, col: int) -> bool:
        """
            Checks that the row and col values are in the range
        """
        if type(row) not in (int,) or type(col) not in (int,):
            raise TypeError('row or col not integers')

        if row < 0 or row >= self.__num_rows:
            raise RuntimeError(f'Row {row} out of bound')
        if col < 0 or col >= self.__num_cols:
            raise RuntimeError(f'Col {col} out of bound')

        return True

    def __is_alive(self, row: int, col: int) -> bool:
        """
            Returns the status of the Cell in the (row, col) position
        """
        if self.__check_limits(row, col):
            return self.__board[row][col].get_alive_status()

    def __get_neighbours_alive(self, row: int, col: int) -> int:
        """
            Returns the number of alive neighbours for the
            Cell in the (row, col) position
        """
        neighbours_alive = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:  # Not the same position
                    if self.__is_alive((row + i) % self.__num_rows, (col + i) % self.__num_cols):
                        neighbours_alive += 1
        return neighbours_alive

    def __is_going_to_be_alive(self, row: int, col: int) -> bool:
        """
            Returns the status of the Cell in the position (row, col)
            for the next generation of the game. Applies the game rules
        """
        if self.__check_limits(row, col):
            alive_neigh = self.__get_neighbours_alive(row, col)
            alive = False
            if ((self.__is_alive(row, col) and ((alive_neigh == 2) or (alive_neigh == 3))
                    or (not self.__is_alive(row, col) and alive_neigh == 3))):
                alive = True

            return alive

    def update_board(self):
        """
            Updates the board with a new iteration of the game
        """
        new_board = []
        for idx in range(0, self.__num_rows):
            new_row = []
            for jdx in range(0, self.__num_cols):
                is_alive = self.__is_going_to_be_alive(idx, jdx)
                new_row.append(Cell(is_alive))
            new_board.append(new_row)

        self.__board.clear()
        self.__board = new_board
