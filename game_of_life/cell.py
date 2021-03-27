

class Cell:
    """
        class Cell to represent a Cell in the Game of Life game
    """

    def __init__(self, alive: bool = False):
        """
            Builds a new Cell with its status
        """
        if type(alive) != bool:
            raise TypeError('Alive status must be a boolean')

        self.__is_alive = alive

    def get_alive_status(self):
        """
            Returns the status of a Cell
        """
        return self.__is_alive

    def __str__(self):
        """
            Returns the string representation of a Cell
            When the Cell is alive it returns *
            otherwise it return o.
        """
        return '*' if self.__is_alive is False else 'o'
