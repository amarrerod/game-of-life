#!/usr/bin/env python

import unittest
from copy import copy
from game_of_life.board import Board


class TestBoard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.emptyBoard = Board()
        cls.board = Board(10, 10)

    @classmethod
    def tearDownClass(cls):
        cls.emptyBoard = None
        cls.board = None

    def test_create_a_board(self):
        self.assertIsInstance(self.board, Board)

    def test_create_a_board_error(self):
        self.assertRaises(TypeError, Board, 25.0, 25.0,
                          msg='num_rows or num_cols not int')

    def test_get_num_rows(self):
        self.assertEqual(self.board.get_num_rows(), 10)
        self.assertEqual(self.emptyBoard.get_num_rows(), 0)

    def test_get_num_cols(self):
        self.assertEqual(self.board.get_num_cols(), 10)
        self.assertEqual(self.emptyBoard.get_num_cols(), 0)

    def test_set_num_rows(self):
        new_rows = 100
        copy_board = copy(self.board)
        copy_board.set_num_rows(new_rows)
        self.assertEqual(copy_board.get_num_rows(), new_rows)
        self.assertEqual(self.board.get_num_rows(), 10)

    def test_set_num_rows_raises(self):
        new_rows = 1000.0
        copy_board = copy(self.board)
        self.assertRaises(TypeError, copy_board.set_num_rows,
                          new_rows, msg='num_rows is not int')

    def test_set_num_cols(self):
        new_cols = 100
        copy_board = copy(self.board)
        copy_board.set_num_cols(new_cols)
        self.assertEqual(copy_board.get_num_cols(), new_cols)
        self.assertEqual(self.board.get_num_rows(), 10)

    def test_set_num_cols_raises(self):
        new_cols = 1000.0
        copy_board = copy(self.board)
        self.assertRaises(TypeError, copy_board.set_num_cols,
                          new_cols, msg='num_rows is not int')

    def test_get_board(self):
        inner_board = self.board.get_board()
        empty_inner_board = self.emptyBoard.get_board()
        self.assertIsInstance(inner_board, list)
        self.assertIsInstance(empty_inner_board, list)
