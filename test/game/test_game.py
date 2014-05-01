__author__ = 'frealgagu'

from unittest import TestCase
from bomberkiller.game.game import Game
from bomberkiller.elements.element import Element
from bomberkiller.game.action import Action
from bomberkiller.game.strategy import Strategy


class TestGame(TestCase):

    def __init__(self, method_name=None):
        super(TestGame, self).__init__(method_name)

    def setUp(self):
        super(TestGame, self).setUp()
        self.game = Game()

    def tearDown(self):
        super(TestGame, self).tearDown()

    def test_game(self):
        pass

    def test_prepare(self):
        self.game.prepare()

    def test_start(self):
        self.game.start(Element.PLAYER_A, "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertIsNotNone(self.game.strategy)
        self.assertIsNotNone(self.game.strategy.board)
        self.assertIsNotNone(self.game.strategy.board.bombs)
        self.assertEqual(len(self.game.strategy.board.bombs), 4)
        self.assertIsNotNone(self.game.strategy.board.enemies)
        self.assertEqual(len(self.game.strategy.board.enemies), 3)
        self.assertIsNotNone(self.game.strategy.board.powers)
        self.assertEqual(len(self.game.strategy.board.powers), 1)
        self.assertIsNotNone(self.game.strategy.board.bomber_killer)
        self.assertTrue(self.game.strategy.board.bomber_killer.is_bomb_range())

    def test_turn(self):
        self.game.strategy = Strategy(Element.PLAYER_A)

        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertIsNotNone(self.game.strategy)
        self.assertIsNotNone(self.game.strategy.board)
        self.assertIsNotNone(self.game.strategy.board.bombs)
        self.assertEqual(len(self.game.strategy.board.bombs), 4)
        self.assertIsNotNone(self.game.strategy.board.enemies)
        self.assertEqual(len(self.game.strategy.board.enemies), 3)
        self.assertIsNotNone(self.game.strategy.board.powers)
        self.assertEqual(len(self.game.strategy.board.powers), 1)
        self.assertIsNotNone(self.game.strategy.board.bomber_killer)
        self.assertTrue(self.game.strategy.board.bomber_killer.is_bomb_range())
        self.assertEquals(self.game.strategy.action, Action.PASS)

        self.game.turn("2", "X,X,X,X,X,X,X,X,X,X,X\n"
                            "X,_,_,_,_,_,_,_,_,_,X\n"
                            "X,_,_,_,_,_,_,_,_,_,X\n"
                            "X,_,_,_,_,_,_,_,_,_,X\n"
                            "X,_,_,_,P,1,B,_,_,_,X\n"
                            "X,_,_,_,1,A,1,_,_,_,X\n"
                            "X,_,_,_,D,1,C,_,_,_,X\n"
                            "X,_,_,_,_,_,_,_,_,_,X\n"
                            "X,_,_,_,_,_,_,_,_,_,X\n"
                            "X,_,_,_,_,_,_,_,_,_,X\n"
                            "X,X,X,X,X,X,X,X,X,X,X")
        self.assertIsNotNone(self.game.strategy)
        self.assertIsNotNone(self.game.strategy.board)
        self.assertIsNotNone(self.game.strategy.board.bombs)
        self.assertEqual(len(self.game.strategy.board.bombs), 4)
        self.assertIsNotNone(self.game.strategy.board.enemies)
        self.assertEqual(len(self.game.strategy.board.enemies), 3)
        self.assertIsNotNone(self.game.strategy.board.powers)
        self.assertEqual(len(self.game.strategy.board.powers), 1)
        self.assertIsNotNone(self.game.strategy.board.bomber_killer)
        self.assertTrue(self.game.strategy.board.bomber_killer.is_bomb_range())
        self.assertEquals(self.game.strategy.action, Action.PASS)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.EAST)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.WEST)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.NORTH)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.SOUTH)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.BOMB_EAST)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.BOMB_WEST)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.BOMB_NORTH)

        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.turn("1", "X,X,X,X,X,X,X,X,X,X,X\n"
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
        self.assertEquals(self.game.strategy.action, Action.BOMB_SOUTH)

    def test_lost(self):
        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.lost()
        self.assertIsNone(self.game.strategy)

    def test_already_connected(self):
        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.already_connected()
        self.assertIsNone(self.game.strategy)

    def test_wrong_messages(self):
        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.wrong_messages(456)
        self.assertIsNone(self.game.strategy)

    def test_end(self):
        self.game.strategy = Strategy(Element.PLAYER_A)
        self.game.end()
        self.assertIsNone(self.game.strategy)