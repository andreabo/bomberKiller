__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from bomberkiller.elements.board import Board
from bomberkiller.elements.element import Element
from bomberkiller.game.action import Action


class TestBoard(TestCase):

    def __init__(self, method_name=None):
        super(TestBoard, self).__init__(method_name)

    def setUp(self):
        self.board = Board()
        self.board.elements = []
        for i in range(0, 9):
            row_elements = []
            for j in range(0, 9):
                row_elements.append(Element(Element.EMPTY_SPACE, i, j))
            self.board.elements.append(row_elements)

    def test_retrieve_element_by_position(self):
        element = Element(Element.BREAKABLE_WALL, 6, 4)
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
        element = Element(Element.BREAKABLE_WALL, 6, 4)
        self.board.elements[4][6] = element

        right_element = Element(Element.PLAYER_A, 7, 4)
        self.board.elements[4][7] = right_element

        left_element = Element(Element.PLAYER_B, 5, 4)
        self.board.elements[4][5] = left_element

        up_element = Element(Element.PLAYER_C, 6, 3)
        self.board.elements[3][6] = up_element

        down_element = Element(Element.PLAYER_D, 6, 5)
        self.board.elements[5][6] = down_element

        new_element = self.board.retrieve_element(element, Action.PASS)
        self.assertEquals(new_element, element)

        new_element = self.board.retrieve_element(element, Action.EAST)
        self.assertEquals(new_element, right_element)

        new_element = self.board.retrieve_element(element, Action.WEST)
        self.assertEquals(new_element, left_element)

        new_element = self.board.retrieve_element(element, Action.NORTH)
        self.assertEquals(new_element, up_element)

        new_element = self.board.retrieve_element(element, Action.SOUTH)
        self.assertEquals(new_element, down_element)

    def test_retrieve_contiguous_elements(self):
        element = Element(Element.BREAKABLE_WALL, 6, 4)
        self.board.elements[4][6] = element

        right_element = Element(Element.PLAYER_A, 7, 4)
        self.board.elements[4][7] = right_element

        left_element = Element(Element.PLAYER_B, 5, 4)
        self.board.elements[4][5] = left_element

        up_element = Element(Element.PLAYER_C, 6, 3)
        self.board.elements[3][6] = up_element

        down_element = Element(Element.PLAYER_D, 6, 5)
        self.board.elements[5][6] = down_element

        elements = self.board.retrieve_contiguous_elements(element)
        print elements
        self.assertEquals(len(elements), 4)
        self.assertEquals(elements[0], right_element)
        self.assertEquals(elements[1], left_element)
        self.assertEquals(elements[2], up_element)
        self.assertEquals(elements[3], down_element)

    def test__repr__(self):
        timer_1_bomb = Element(Element.EMPTY_SPACE, 0, 0)
        timer_1_bomb.bomb_threat = Element(Element.EMPTY_SPACE, 0, 0)
        self.board.elements[0][0] = timer_1_bomb

        timer_1_bomb = Element(Element.EMPTY_SPACE, 1, 1)
        timer_1_bomb.bomb_threat = Element(Element.TIMER_1_LEFT_BOMB, 1, 1)
        self.board.elements[1][1] = timer_1_bomb

        timer_2_bomb = Element(Element.EMPTY_SPACE, 2, 2)
        timer_2_bomb.bomb_threat = Element(Element.TIMER_2_LEFT_BOMB, 2, 2)
        self.board.elements[2][2] = timer_2_bomb

        element = Element(Element.BREAKABLE_WALL, 6, 4)
        self.board.elements[4][6] = element

        right_element = Element(Element.PLAYER_A, 7, 4)
        self.board.elements[4][7] = right_element

        left_element = Element(Element.PLAYER_B, 5, 4)
        self.board.elements[4][5] = left_element

        up_element = Element(Element.PLAYER_C, 6, 3)
        self.board.elements[3][6] = up_element

        down_element = Element(Element.PLAYER_D, 6, 5)
        self.board.elements[5][6] = down_element

        self.assertEquals(self.board.__repr__(),
                          "| ?. . . . . . . .  |\n"
                          "|  .$. . . . . . .  |\n"
                          "|  . .*. . . . . .  |\n"
                          "|  . . . . . .C. .  |\n"
                          "|  . . . . .B.W.A.  |\n"
                          "|  . . . . . .D. .  |\n"
                          "|  . . . . . . . .  |\n"
                          "|  . . . . . . . .  |\n"
                          "|  . . . . . . . .  |")