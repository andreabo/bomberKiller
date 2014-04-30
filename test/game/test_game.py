__author__ = 'frealgagu'

from unittest import TestCase
from bomberkiller.game.game import Game


class TestGame(TestCase):

    def __init__(self):
        super(TestGame, self).__init__()

    def setUp(self):
        super(TestGame, self).setUp()
        self.game = Game()

    def tearDown(self):
        super(TestGame, self).tearDown()

    def test_game(self):
        pass

