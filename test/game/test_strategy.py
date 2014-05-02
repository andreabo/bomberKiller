__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from pymock.pymock import Controller
from bomberkiller.game.strategy import Strategy
from bomberkiller.elements.element import Element
from bomberkiller.game.action import Action


class TestStrategy(TestCase):
    def __init__(self, method_name=None):
        super(TestStrategy, self).__init__(method_name)

    def setUp(self):
        super(TestStrategy, self).setUp()
        self.controller = Controller()
        self.strategy = Strategy(Element.PLAYER_A)

    def tearDown(self):
        super(TestStrategy, self).tearDown()

    def test_strategy(self):
        pass

    def test_create_board(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,P,2,B,_,_,_,X\n"
                                   "X,_,_,_,2,A,2,_,_,_,X\n"
                                   "X,_,_,_,D,2,C,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.assertIsNotNone(self.strategy.board)
        self.assertIsNotNone(self.strategy.board.elements)
        self.assertEquals(len(self.strategy.board.elements), 11)
        for row_number in range(0, 10):
            self.assertEquals(len(self.strategy.board.elements[row_number]), 11)
        self.assertIsNone(self.strategy.board.bomber_killer)
        self.assertEquals(len(self.strategy.board.enemies), 0)
        self.assertEquals(len(self.strategy.board.powers), 0)
        self.assertEquals(len(self.strategy.board.bombs), 0)

    def test_locate_elements(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,P,2,B,_,_,_,X\n"
                                   "X,_,_,_,2,A,2,_,_,_,X\n"
                                   "X,_,_,_,D,2,C,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertIsNotNone(self.strategy.board.bomber_killer)
        self.assertEquals(len(self.strategy.board.enemies), 3)
        self.assertEquals(len(self.strategy.board.powers), 1)
        self.assertEquals(len(self.strategy.board.bombs), 4)

    def test_update_rules_information(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,A,V,P,P,V,P,D,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,P,_,_,_,_,_,V,_,X\n"
                                   "X,_,P,_,_,_,_,_,V,_,X\n"
                                   "X,_,B,_,_,_,_,_,C,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.update_rules_information()
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_A], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_B], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_C], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_D], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_A], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_B], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_C], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_D], 1)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,A,P,P,V,D,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,P,_,_,_,_,_,V,_,X\n"
                                   "X,_,B,_,_,_,_,_,C,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.update_rules_information()
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_A], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_B], 2)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_C], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_D], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_A], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_B], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_C], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_D], 1)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,A,P,D,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,B,_,_,_,_,_,C,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.update_rules_information()
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_A], 2)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_B], 3)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_C], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_D], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_A], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_B], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_C], 3)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_D], 2)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,A,D,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,B,_,_,_,C,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.update_rules_information()
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_A], 3)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_B], 3)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_C], 1)
        self.assertEquals(self.strategy.rules.players_bomb_magnitude[Element.PLAYER_D], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_A], 2)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_B], 1)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_C], 3)
        self.assertEquals(self.strategy.rules.players_bombs_quantity[Element.PLAYER_D], 2)

    def test_calculate_bomb_ranges(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,P,2,B,_,_,_,X\n"
                                   "X,_,_,_,_,A,2,_,_,_,X\n"
                                   "X,_,_,_,D,_,C,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,P,1,B,_,_,_,X\n"
                                   "X,_,_,_,2,A,1,_,_,_,X\n"
                                   "X,_,_,_,D,2,C,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,L,X,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.rules.players_bomb_magnitude = \
            {
                Element.PLAYER_A: 1,
                Element.PLAYER_B: 2,
                Element.PLAYER_C: 3,
                Element.PLAYER_D: 5
            }
        self.strategy.calculate_bomb_ranges()
        self.assertTrue(self.strategy.board.elements[1][4].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[1][5].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[1][6].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[4][1].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[5][1].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[6][1].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[4][9].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[5][9].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[6][9].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[10][4].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[10][5].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[10][6].is_bomb_range())

        self.assertTrue(self.strategy.board.elements[4][4].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[4][5].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[4][6].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[5][4].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[5][5].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[5][6].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[6][4].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[6][5].is_bomb_range())
        self.assertTrue(self.strategy.board.elements[6][6].is_bomb_range())

        self.assertFalse(self.strategy.board.elements[3][3].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[3][7].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[7][3].is_bomb_range())
        self.assertFalse(self.strategy.board.elements[7][7].is_bomb_range())

    def test_calculate_effort(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,_,X,_,_,_,_,_,X\n"
                                   "X,_,X,_,X,_,_,_,_,_,X\n"
                                   "X,L,_,_,X,_,_,_,_,_,X\n"
                                   "X,_,X,_,X,_,_,_,_,_,X\n"
                                   "X,_,L,_,X,_,_,_,_,_,X\n"
                                   "X,P,_,_,X,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_effort()
        self.assertEquals(self.strategy.board.elements[6][1].move_effort, 25)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,_,X,_,_,_,_,_,X\n"
                                   "X,_,X,_,X,_,_,_,_,_,X\n"
                                   "X,X,_,_,X,_,_,_,_,_,X\n"
                                   "X,_,X,_,X,_,_,_,_,_,X\n"
                                   "X,_,L,_,X,_,_,_,_,_,X\n"
                                   "X,P,_,_,X,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_effort()
        self.assertEquals(self.strategy.board.elements[6][1].move_effort, 35)

    def test_issue(self):
        self.strategy.player_character = Element.PLAYER_D
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,#,_,C,_,_,X\n"
                                   "X,_,_,_,#,#,#,_,_,_,X\n"
                                   "X,L,L,L,_,#,_,_,_,L,X\n"
                                   "X,_,L,_,_,_,_,_,_,L,X\n"
                                   "X,_,_,_,_,_,_,B,_,_,X\n"
                                   "X,_,_,_,_,_,L,_,_,_,X\n"
                                   "X,_,A,2,D,_,L,_,_,_,X\n"
                                   "X,_,_,_,_,_,L,L,_,_,X\n"
                                   "X,_,_,_,L,_,L,L,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,#,_,C,_,_,X\n"
                                   "X,_,_,_,#,#,#,_,_,_,X\n"
                                   "X,L,L,L,_,#,_,_,_,L,X\n"
                                   "X,_,L,_,_,_,_,_,_,L,X\n"
                                   "X,_,_,_,_,_,_,B,_,_,X\n"
                                   "X,_,2,_,2,_,L,_,_,_,X\n"
                                   "X,_,A,1,D,_,L,_,_,_,X\n"
                                   "X,_,_,_,_,_,L,L,_,_,X\n"
                                   "X,_,_,_,L,_,L,L,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.update_rules_information()
        self.strategy.rules.players_bomb_magnitude = \
            {
                Element.PLAYER_A: 2,
                Element.PLAYER_B: 1,
                Element.PLAYER_C: 1,
                Element.PLAYER_D: 3
            }
        self.strategy.calculate_bomb_ranges()
        self.strategy.calculate_effort()
        self.strategy.calculate_action()
        print self.strategy.board.elements[8][4]
        print self.strategy.board.elements[7][4]
        print self.strategy.board.elements[6][4]
        print self.strategy.board

    def test_calculate_action(self):
        self.strategy.rules.players_bomb_magnitude = \
            {
                Element.PLAYER_A: 1,
                Element.PLAYER_B: 2,
                Element.PLAYER_C: 3,
                Element.PLAYER_D: 5
            }
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,A,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.strategy.calculate_effort()
        self.strategy.calculate_action()

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,X,X,X,_,_,_,_,X\n"
                                   "X,_,X,_,A,_,P,2,B,_,X\n"
                                   "X,_,X,X,X,X,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,X,X,X,_,_,_,_,X\n"
                                   "X,_,X,_,_,A,P,1,_,B,X\n"
                                   "X,_,X,X,X,X,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.strategy.calculate_effort()
        self.strategy.calculate_action()

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,C,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,X,_,_,_,_,X\n"
                                   "X,_,X,D,A,_,P,2,_,_,X\n"
                                   "X,#,#,#,#,_,_,B,_,_,X\n"
                                   "X,_,#,_,_,_,_,_,_,_,X\n"
                                   "X,_,#,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,C,_,_,_,_,_,X\n"
                                   "X,_,X,_,2,X,_,_,_,_,X\n"
                                   "X,_,X,D,_,A,P,1,_,_,X\n"
                                   "X,_,X,_,_,_,B,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.strategy.calculate_effort()
        self.strategy.calculate_action()

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,C,_,_,_,#,_,_,X\n"
                                   "X,_,X,_,1,X,_,#,_,_,X\n"
                                   "X,_,X,D,A,#,#,#,#,#,X\n"
                                   "X,_,X,_,_,B,_,#,_,_,X\n"
                                   "X,_,_,_,_,_,_,#,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.strategy.calculate_effort()
        self.strategy.calculate_action()

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,C,_,_,_,_,_,_,X\n"
                                   "X,_,X,2,1,X,_,_,_,_,X\n"
                                   "X,_,X,A,_,_,_,_,_,_,X\n"
                                   "X,_,X,D,2,B,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,#,_,_,_,_,_,X\n"
                                   "X,_,_,_,#,_,_,_,_,_,X\n"
                                   "X,_,C,_,#,_,_,_,_,_,X\n"
                                   "X,_,X,1,#,X,_,_,_,_,X\n"
                                   "X,_,X,A,#,_,_,_,_,_,X\n"
                                   "X,_,X,_,1,_,_,_,_,_,X\n"
                                   "X,_,_,D,_,B,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.strategy.calculate_effort()
        self.strategy.calculate_action()

    def test_move_or_put_a_bomb(self):
        self.strategy.random = self.controller.mock()
        self.controller.expectAndReturn(self.strategy.random.random(), 0.1)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.3)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.5)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.7)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.9)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.1)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.3)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.5)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.7)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.9)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.1)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.3)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.5)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.7)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.9)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.1)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.3)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.5)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.7)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.9)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.1)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.3)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.5)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.7)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.9)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.expectAndReturn(self.strategy.random.random(), 0.0)
        self.controller.replay()

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,B,_,_,_,_,_,_,X\n"
                                   "X,_,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        next_place = self.strategy.board.elements[1][2]
        path = [self.strategy.board.elements[1][2],
                self.strategy.board.elements[1][3]]

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,_,B,_,_,_,_,_,X\n"
                                   "X,_,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        next_place = self.strategy.board.elements[1][2]
        path = [self.strategy.board.elements[1][2],
                self.strategy.board.elements[1][3],
                self.strategy.board.elements[1][4]]

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,_,_,B,_,_,_,_,X\n"
                                   "X,_,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        next_place = self.strategy.board.elements[1][2]
        path = [self.strategy.board.elements[1][2],
                self.strategy.board.elements[1][3],
                self.strategy.board.elements[1][4],
                self.strategy.board.elements[1][5]]

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,_,_,_,B,_,_,_,X\n"
                                   "X,_,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        next_place = self.strategy.board.elements[1][2]
        path = [self.strategy.board.elements[1][2],
                self.strategy.board.elements[1][3],
                self.strategy.board.elements[1][4],
                self.strategy.board.elements[1][5],
                self.strategy.board.elements[1][6]]

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,A,_,_,_,_,_,B,_,_,X\n"
                                   "X,_,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,_,X,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        next_place = self.strategy.board.elements[1][2]
        path = [self.strategy.board.elements[1][2],
                self.strategy.board.elements[1][3],
                self.strategy.board.elements[1][4],
                self.strategy.board.elements[1][5],
                self.strategy.board.elements[1][6],
                self.strategy.board.elements[1][7]]

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.BOMB_EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.EAST)

        self.strategy.board.elements[1][1].individual_effort = 50
        self.strategy.board.elements[1][2].individual_effort = 50

        action = self.strategy.move_or_put_a_bomb(next_place, path)
        self.assertEquals(action, Action.PASS)

    def test_move_to(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,C,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,L,L,L,_,_,_,X\n"
                                   "X,_,_,B,L,A,_,_,_,_,X\n"
                                   "X,_,_,_,L,L,L,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,D,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.move_to(self.strategy.board.elements[5][6])
        self.assertEquals(action, Action.EAST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,C,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,L,L,L,_,_,_,X\n"
                                   "X,_,_,_,_,A,L,B,_,_,X\n"
                                   "X,_,_,_,L,L,L,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,D,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.move_to(self.strategy.board.elements[5][4])
        self.assertEquals(action, Action.WEST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,C,_,_,_,_,_,_,_,D,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,L,_,L,_,_,_,X\n"
                                   "X,_,_,_,L,A,L,_,_,_,X\n"
                                   "X,_,_,_,L,L,L,_,_,_,X\n"
                                   "X,_,_,_,_,B,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.move_to(self.strategy.board.elements[4][5])
        self.assertEquals(action, Action.NORTH)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,B,_,_,_,_,X\n"
                                   "X,_,_,_,L,L,L,_,_,_,X\n"
                                   "X,_,_,_,L,A,L,_,_,_,X\n"
                                   "X,_,_,_,L,_,L,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,C,_,_,_,_,_,_,_,D,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.move_to(self.strategy.board.elements[6][5])
        self.assertEquals(action, Action.SOUTH)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,X,_,_,_,_,X\n"
                                   "X,_,_,_,X,A,X,_,_,_,X\n"
                                   "X,_,_,_,_,X,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.move_to(self.strategy.board.elements[5][5])
        self.assertEquals(action, Action.PASS)

    def test_put_a_bomb_on(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,L,L,L,L,L,X\n"
                                   "X,_,_,_,_,L,_,L,C,D,X\n"
                                   "X,_,_,_,_,L,_,A,_,B,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.put_a_bomb_on(self.strategy.board.elements[9][8])
        self.assertEquals(action, Action.BOMB_EAST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,B,_,A,_,L,_,_,_,_,X\n"
                                   "X,C,D,L,_,L,_,_,_,_,X\n"
                                   "X,L,L,L,L,L,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.put_a_bomb_on(self.strategy.board.elements[1][2])
        self.assertEquals(action, Action.BOMB_WEST)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,L,C,B,X\n"
                                   "X,_,_,_,_,_,_,L,D,_,X\n"
                                   "X,_,_,_,_,_,_,L,L,A,X\n"
                                   "X,_,_,_,_,_,_,L,_,_,X\n"
                                   "X,_,_,_,_,_,_,L,L,L,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.put_a_bomb_on(self.strategy.board.elements[2][9])
        self.assertEquals(action, Action.BOMB_NORTH)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,L,L,L,_,_,_,_,_,_,X\n"
                                   "X,_,_,L,_,_,_,_,_,_,X\n"
                                   "X,A,L,L,_,_,_,_,_,_,X\n"
                                   "X,_,C,L,_,_,_,_,_,_,X\n"
                                   "X,B,D,L,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.put_a_bomb_on(self.strategy.board.elements[8][1])
        self.assertEquals(action, Action.BOMB_SOUTH)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,X,_,_,_,_,X\n"
                                   "X,_,_,_,X,A,X,_,_,_,X\n"
                                   "X,_,_,_,_,X,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        action = self.strategy.put_a_bomb_on(self.strategy.board.elements[5][5])
        self.assertEquals(action, Action.PASS)

    def test_retrieve_possible_put_players(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,A,_,_,_,_,X\n"
                                   "X,_,_,_,_,2,B,_,_,_,X\n"
                                   "X,_,_,_,D,_,C,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        bomb = self.strategy.board.bombs[0]
        possible_players = self.strategy.retrieve_possible_put_players(bomb)
        self.assertEquals(len(possible_players), 2)
        self.assertEquals(possible_players[0].type, Element.PLAYER_B)
        self.assertEquals(possible_players[1].type, Element.PLAYER_A)

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,A,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,D,1,_,_,_,_,X\n"
                                   "X,_,_,_,_,C,B,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        bomb = self.strategy.board.bombs[0]
        possible_players = self.strategy.retrieve_possible_put_players(bomb)
        self.assertEquals(len(possible_players), 2)
        self.assertEquals(possible_players[0].type, Element.PLAYER_B)
        self.assertEquals(possible_players[1].type, Element.PLAYER_A)

    def test_can_put_bomb(self):
        self.strategy.rules.players_bombs_quantity = \
            {
                Element.PLAYER_A: 3,
                Element.PLAYER_B: 1,
                Element.PLAYER_C: 1,
                Element.PLAYER_D: 1
            }

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,A,_,_,_,_,_,_,_,X\n"
                                   "X,_,2,_,_,_,_,_,_,_,X\n"
                                   "X,_,B,C,D,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertTrue(self.strategy.can_put_bomb())

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,A,_,_,_,_,_,_,X\n"
                                   "X,_,1,2,_,_,_,_,_,_,X\n"
                                   "X,_,B,C,D,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertTrue(self.strategy.can_put_bomb())

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,#,_,A,_,_,_,_,_,X\n"
                                   "X,#,#,1,2,_,_,_,_,_,X\n"
                                   "X,_,b,C,D,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertFalse(self.strategy.can_put_bomb())

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,#,_,A,_,_,_,_,X\n"
                                   "X,_,#,#,1,_,_,_,_,_,X\n"
                                   "X,_,_,c,D,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertTrue(self.strategy.can_put_bomb())

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,#,_,A,_,_,_,X\n"
                                   "X,_,_,#,1,#,_,_,_,_,X\n"
                                   "X,_,_,_,d,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertTrue(self.strategy.can_put_bomb())

    def test_predict_safety_after_put_a_bomb(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertTrue(self.strategy.predict_safety_after_put_a_bomb(self.strategy.board.elements[4][5]))

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertFalse(self.strategy.predict_safety_after_put_a_bomb(self.strategy.board.elements[4][5]))

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,B,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.assertFalse(self.strategy.predict_safety_after_put_a_bomb(self.strategy.board.elements[4][5]))

    def test_predict_safety_after_move(self):
        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.assertTrue(self.strategy.predict_safety_after_move(self.strategy.board.elements[4][5]))

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,1,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.assertTrue(self.strategy.predict_safety_after_move(self.strategy.board.elements[4][5]))

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,1,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.assertTrue(self.strategy.predict_safety_after_move(self.strategy.board.elements[4][5]))

        self.strategy.create_board("X,X,X,X,X,X,X,X,X,X,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,X,B,X,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,A,1,_,_,_,X\n"
                                   "X,_,_,_,X,_,X,_,_,_,X\n"
                                   "X,_,_,_,X,X,X,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,_,_,_,_,_,_,_,_,_,X\n"
                                   "X,X,X,X,X,X,X,X,X,X,X")
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.assertFalse(self.strategy.predict_safety_after_move(self.strategy.board.elements[4][5]))