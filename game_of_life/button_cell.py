
from tkinter import Button
from game_of_life.cell import Cell


class ButtonCell(Button):
    def __init__(self, *args, **kargs):
        Button.__init__(self, *args, **kargs)
        self.__cell = Cell(False)
        self['command'] = self.__toggle

    def __toggle(self):
        if self['bg'] == "white":
            self['bg'] = "black"
            self.__cell = Cell(True)
        else:
            self['bg'] = "white"
            self.__cell = Cell(False)
