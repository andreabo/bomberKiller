__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from bomberkiller.elements.board import Board
from bomberkiller.elements.element import Element


class TestBoard(TestCase):

    def __init__(self, method_name=None):
        super(TestBoard, self).__init__(method_name)

    def setUp(self):
        self.board = Board()
        self.board.elements = []
        for i in range(0, 9):
            row_elements = []
            for j in range(0, 9):
                row_elements.append(Element('_', i, j))
            self.board.elements.append(row_elements)

    def test_retrieve_element_by_position(self):
        element = Element('L', 6, 4)
        self.board.elements[4][6] = element

        new_element = self.board.retrieve_element_by_position(6, 4)
        self.assertEquals(new_element, element)

        new_element = self.board.retrieve_element_by_position(11, 4)
        self.assertEquals(new_element, None)

        new_element = self.board.retrieve_element_by_position(6, 11)
        self.assertEquals(new_element, None)

        new_element = self.board.retrieve_element_by_position(-1, 4)
        self.assertEquals(new_element, None)

        new_element = self.board.retrieve_element_by_position(6, -1)
        self.assertEquals(new_element, None)

        new_element = self.board.retrieve_element_by_position(11, 11)
        self.assertEquals(new_element, None)

        new_element = self.board.retrieve_element_by_position(-1, -1)
        self.assertEquals(new_element, None)

    def test_retrieve_element(self):
        element = Element('L', 6, 4)
        self.board.elements[4][6] = element

    def test_retrieve_contiguous_elements(self):
        pass