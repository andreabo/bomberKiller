__author__ = 'frealgagu'

from unittest import TestCase
from bomberkiller.game.rules import Rules
from bomberkiller.elements.element import Element


class TestRules(TestCase):

    def __init__(self, method_name=None):
        super(TestRules, self).__init__(method_name)

    def setUp(self):
        super(TestRules, self).setUp()
        self.rules = Rules()

    def tearDown(self):
        super(TestRules, self).tearDown()

    def test_rules(self):
        pass

    def test_retrieve_max_bomb_magnitude(self):
        self.rules.players_bomb_magnitude = \
            {
                Element.PLAYER_A: 2,
                Element.PLAYER_B: 4,
                Element.PLAYER_C: 3,
                Element.PLAYER_D: 1
            }

        player_a = Element(Element.PLAYER_A, 6, 5)
        player_b = Element(Element.PLAYER_B, 4, 5)
        player_c = Element(Element.PLAYER_C, 5, 4)
        player_d = Element(Element.PLAYER_D, 5, 6)

        magnitude = self.rules.retrieve_max_bomb_magnitude([player_a, player_b, player_c, player_d])
        self.assertEquals(magnitude, 4)

        magnitude = self.rules.retrieve_max_bomb_magnitude([player_a, player_c, player_d])
        self.assertEquals(magnitude, 3)

        magnitude = self.rules.retrieve_max_bomb_magnitude([player_d])
        self.assertEquals(magnitude, 1)

    def test_retrieve_bombs_quantity(self):
        self.rules.players_bombs_quantity = \
            {
                Element.PLAYER_A: 2,
                Element.PLAYER_B: 4,
                Element.PLAYER_C: 3,
                Element.PLAYER_D: 1
            }

        element = Element(Element.PLAYER_A, 5, 5)
        quantity = self.rules.retrieve_bombs_quantity(element)
        self.assertEquals(quantity, 2)

        element = Element(Element.PLAYER_B, 5, 5)
        quantity = self.rules.retrieve_bombs_quantity(element)
        self.assertEquals(quantity, 4)

        element = Element(Element.PLAYER_C, 5, 5)
        quantity = self.rules.retrieve_bombs_quantity(element)
        self.assertEquals(quantity, 3)

        element = Element(Element.PLAYER_D, 5, 5)
        quantity = self.rules.retrieve_bombs_quantity(element)
        self.assertEquals(quantity, 1)

    def test_increase_bomb_magnitude(self):
        self.rules.players_bomb_magnitude = \
            {
                Element.PLAYER_A: 2,
                Element.PLAYER_B: 4,
                Element.PLAYER_C: 3,
                Element.PLAYER_D: 1
            }

        element = Element(Element.PLAYER_A, 5, 5)
        self.rules.increase_bomb_magnitude(element)
        self.assertEquals(self.rules.players_bomb_magnitude[Element.PLAYER_A], 3)

        element = Element(Element.PLAYER_B, 5, 5)
        self.rules.increase_bomb_magnitude(element)
        self.assertEquals(self.rules.players_bomb_magnitude[Element.PLAYER_B], 5)

        element = Element(Element.PLAYER_C, 5, 5)
        self.rules.increase_bomb_magnitude(element)
        self.assertEquals(self.rules.players_bomb_magnitude[Element.PLAYER_C], 4)

        element = Element(Element.PLAYER_D, 5, 5)
        self.rules.increase_bomb_magnitude(element)
        self.assertEquals(self.rules.players_bomb_magnitude[Element.PLAYER_D], 2)

    def test_increase_bombs_quantity(self):
        self.rules.players_bombs_quantity = \
            {
                Element.PLAYER_A: 2,
                Element.PLAYER_B: 4,
                Element.PLAYER_C: 3,
                Element.PLAYER_D: 1
            }

        element = Element(Element.PLAYER_A, 5, 5)
        self.rules.increase_bombs_quantity(element)
        self.assertEquals(self.rules.players_bombs_quantity[Element.PLAYER_A], 3)

        element = Element(Element.PLAYER_B, 5, 5)
        self.rules.increase_bombs_quantity(element)
        self.assertEquals(self.rules.players_bombs_quantity[Element.PLAYER_B], 5)

        element = Element(Element.PLAYER_C, 5, 5)
        self.rules.increase_bombs_quantity(element)
        self.assertEquals(self.rules.players_bombs_quantity[Element.PLAYER_C], 4)

        element = Element(Element.PLAYER_D, 5, 5)
        self.rules.increase_bombs_quantity(element)
        self.assertEquals(self.rules.players_bombs_quantity[Element.PLAYER_D], 2)