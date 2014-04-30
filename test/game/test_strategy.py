__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from bomberkiller.game.strategy import Strategy
from bomberkiller.elements.element import Element


class TestStrategy(TestCase):

    def __init__(self, method_name=None):
        super(TestStrategy, self).__init__(method_name)

    def setUp(self):
        super(TestStrategy, self).setUp()
        self.strategy = Strategy(Element.PLAYER_A)

    def tearDown(self):
        super(TestStrategy, self).tearDown()

    def test_strategy(self):
        pass