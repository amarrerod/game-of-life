

from tkinter import Frame, Label, Button
from tkinter import TOP, BOTTOM, SUNKEN, W, E
from tkinter import font
from game_of_life.board import Board
from game_of_life.player import Player
from game_of_life.button_cell import ButtonCell


class GUI(Frame):
    def __init__(self, parent, player: Player, board: Board):
        Frame.__init__(self, parent)
        self.__parent = parent
        self.__player = player
        self.__board = board
        self.grid(row=0, column=0)
        self.__size_x = self.__board.get_num_rows()
        self.__size_y = self.__board.get_num_cols()

        self.__build_gui()

    def __build_gui(self):
        self.__parent.title('Game of Life')
        self.title_frame = Frame(self.__parent)
        self.title_frame.grid(row=0, column=0, columnspan=4)
        self.title_font = font.Font(family="Helvetica", size=14)
        title = Label(self.title_frame,
                      text="Conway's Game of Life", font=self.title_font)
        title.pack(side=TOP)

        prompt = Label(
            self.title_frame, text="Click the cells to create the starting configuration")
        prompt.pack(side=BOTTOM)
        self.__build_board()

    def __build_board(self):
        self.board_frame = Frame(self.__parent, width=self.__size_x + 2,
                                 height=self.__size_y + 2, borderwidth=1, relief=SUNKEN)
        self.board_frame.grid(row=2, column=0, columnspan=4)
        self.cell_buttons = [[Button(self.board_frame, bg="white", width=2, height=1) for i in range(
            self.__size_x + 2)] for j in range(self.__size_y + 2)]
        # creates 2d array of buttons for grid
        for i in range(1, self.__size_y + 1):
            for j in range(1, self.__size_x + 1):
                self.cell_buttons[i][j].grid(row=i, column=j, sticky=W+E)
