"""Main module."""

from game_of_life.player import Player

sample = 'game_of_life/worlds/sample2.board'
player = Player()
player.initialise_board(sample)
player.play()
