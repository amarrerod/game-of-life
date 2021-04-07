

from game_of_life.board import Board


class Player:

    def __init__(self, iterations=100):
        self.iterations = iterations
        self.board = Board()
        self.initialised = False

    def initialise_board(self, filename):
        self.board.read_from_file(filename)
        self.initialised = True

    def play(self, verbose=True):
        if self.initialised:
            for _ in range(0, self.iterations):
                if verbose:
                    print(self.board)
                self.board.update_board()
        else:
            print(f'The board must be initialised first')
