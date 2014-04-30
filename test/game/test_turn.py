__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from bomberkiller.game.turn import Turn


class TestTurn(TestCase):

    def __init__(self, method_name=None):
        super(TestTurn, self).__init__(method_name)

    def setUp(self):
        super(TestTurn, self).setUp()
        self.turn = Turn()

    def tearDown(self):
        super(TestTurn, self).tearDown()

    def test_turn(self):
        pass