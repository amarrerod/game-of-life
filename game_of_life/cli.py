"""Console script for game_of_life."""
import argparse
import sys
from tkinter import Tk
from game_of_life.player import Player
from game_of_life.board import Board
from game_of_life.gui import GUI


def main():
    """Console script for game_of_life."""
    parser = argparse.ArgumentParser()
    parser.add_argument('rows', type=int, help="Number of rows in the board")
    parser.add_argument('cols', type=int, help="Number of cols in the board")
    args = parser.parse_args()

    rows = args.rows
    cols = args.cols

    player = Player(int(1e3))
    board = Board(rows, cols)
    player.set_board(board)

    root = Tk()
    game_gui = GUI(root, player, board)
    root.mainloop()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
