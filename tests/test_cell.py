#!/usr/bin/env python

import unittest
from game_of_life.cell import Cell


class TestCell(unittest.TestCase):

    def test_create_a_cell(self):
        alive_cell = Cell(True)
        self.assertTrue(alive_cell.get_alive_status())

    def test_create_death_cell(self):
        death_cell = Cell(False)
        self.assertFalse(death_cell.get_alive_status())

    def test_raise_error_in_init(self):
        self.assertRaises(TypeError, Cell, 'Alive',
                          msg='Alive status must be a boolean')

    def test_get_str_alive(self):
        alive_cell = Cell(True)
        self.assertEqual(str(alive_cell), 'o')

    def test_get_str_death(self):
        death_cell = Cell(False)
        self.assertEqual(str(death_cell), '*')
