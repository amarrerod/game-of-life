

from game_of_life.board import Board


class Player:

    def __init__(self, iterations=100):
        self.__iterations = iterations
        self.__board = Board()
        self.__initialised = False

    def initialise_board(self, filename):
        self.__board.read_from_file(filename)
        self.__initialised = True

    def set_board(self, board: Board):
        self.__board = board

    def get_board(self):
        return self.__board

    def play(self, verbose=True):
        if self.__initialised:
            for _ in range(0, self.__iterations):
                if verbose:
                    print(self.__board)
                self.__board.update_board()
        else:
            print(f'The board must be initialised first')
