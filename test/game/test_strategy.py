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

    def _test_create_board(self, map_):
        self.strategy.create_board(map_)

    def _test_locate_elements(self):
        self.strategy.locate_elements()

    def _test_update_rules_information(self):
        self.strategy.update_rules_information()

    def _test_calculate_bomb_ranges(self):
        self.strategy.calculate_bomb_ranges()

    def _test_calculate_effort(self):
        self.strategy.calculate_effort()

    def _calculate_action(self):
        self.strategy.calculate_action()

    def _test_move_or_put_a_bomb(self, next_place, path):
        self.strategy.move_or_put_a_bomb(next_place, path)

    def _test_move_to(self, next_element):
        self.strategy.move_to(next_element)

    def _put_a_bomb_on(self, next_element):
        self.strategy.put_a_bomb_on(next_element)

    def _test_retrieve_possible_put_players(self, bomb):
        self.strategy.retrieve_possible_put_players(bomb)

    def _test_can_put_bomb(self):
        self.strategy.can_put_bomb()

    def _test_predict_safety_after_put_a_bomb(self, bomb_place):
        self.strategy.predict_safety_after_put_a_bomb(bomb_place)

    def _test_predict_safety_after_move(self, next_place):
        self.strategy.predict_safety_after_move(next_place)