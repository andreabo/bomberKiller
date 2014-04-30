__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from bomberkiller.elements.element import Element


class TestElement(TestCase):

    def __init__(self, method_name=None):
        super(TestElement, self).__init__(method_name)

    def setUp(self):
        super(TestElement, self).setUp()
        self.element = Element(Element.EMPTY_SPACE, 0, 0)

    def tearDown(self):
        super(TestElement, self).tearDown()

    def test_element(self):
        pass

    def test_change_type(self):
        self.element.change_type(Element.FIRE_BOMB_POWER)
        self.assertEquals(self.element.type, Element.FIRE_BOMB_POWER)

    def test_reset_individual_effort(self):
        self.element.type = Element.EMPTY_SPACE
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 4)

        self.element.type = Element.BREAKABLE_WALL
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 10)

        self.element.type = Element.SOLID_WALL
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 9999)

        self.element.type = Element.FIRE_BOMB_POWER
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 1)

        self.element.type = Element.EXTRA_BOMB_POWER
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 1)

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 30)

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 50)

        self.element.type = Element.BOMB_FIRE
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 80)

        self.element.type = Element.PLAYER_A
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 2)

        self.element.type = Element.PLAYER_B
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 2)

        self.element.type = Element.PLAYER_C
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 2)

        self.element.type = Element.PLAYER_D
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 2)

        self.element.type = Element.PLAYER_A_DIED
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 4)

        self.element.type = Element.PLAYER_B_DIED
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 4)

        self.element.type = Element.PLAYER_C_DIED
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 4)

        self.element.type = Element.PLAYER_D_DIED
        self.element.individual_effort = 8765
        self.element.reset_individual_effort()
        self.assertEquals(self.element.individual_effort, 4)

    def test_increase_effort(self):
        self.element.individual_effort = 1234
        self.element.increase_effort(8765)
        self.assertEquals(self.element.individual_effort, 9999)

        self.element.individual_effort = 1234
        self.element.increase_effort(0)
        self.assertEquals(self.element.individual_effort, 1234)

        self.element.individual_effort = 1234
        self.element.increase_effort(-1234)
        self.assertEquals(self.element.individual_effort, 0)

    def test_is_bomb_range(self):
        self.element.bomb_threat = None
        self.assertFalse(self.element.is_bomb_range())

        self.element.bomb_threat = Element(Element.TIMER_1_LEFT_BOMB, 0, 0)
        self.assertTrue(self.element.is_bomb_range())

    def test_is_empty_space(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertTrue(self.element.is_empty_space())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_empty_space())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_empty_space())

    def test_is_breakable_wall(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.BREAKABLE_WALL
        self.assertTrue(self.element.is_breakable_wall())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_breakable_wall())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_breakable_wall())

    def test_is_solid_wall(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.SOLID_WALL
        self.assertTrue(self.element.is_solid_wall())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_solid_wall())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_solid_wall())

    def test_is_wall(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.BREAKABLE_WALL
        self.assertTrue(self.element.is_wall())

        self.element.type = Element.SOLID_WALL
        self.assertTrue(self.element.is_wall())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_wall())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_wall())

    def test_is_power(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_power())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_power())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_power())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertTrue(self.element.is_power())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertTrue(self.element.is_power())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_power())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_power())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_power())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_power())

    def test_is_bomb(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertTrue(self.element.is_bomb())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertTrue(self.element.is_bomb())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_bomb())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_bomb())

    def test_is_bomb_fire(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.BOMB_FIRE
        self.assertTrue(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_bomb_fire())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_bomb_fire())

    def test_is_alive_player(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.PLAYER_A
        self.assertTrue(self.element.is_alive_player())

        self.element.type = Element.PLAYER_B
        self.assertTrue(self.element.is_alive_player())

        self.element.type = Element.PLAYER_C
        self.assertTrue(self.element.is_alive_player())

        self.element.type = Element.PLAYER_D
        self.assertTrue(self.element.is_alive_player())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_alive_player())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_alive_player())

    def test_is_player(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_player())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_player())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_player())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_player())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_player())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_player())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_player())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_player())

        self.element.type = Element.PLAYER_A
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_B
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_C
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_D
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_A_DIED
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_B_DIED
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_C_DIED
        self.assertTrue(self.element.is_player())

        self.element.type = Element.PLAYER_D_DIED
        self.assertTrue(self.element.is_player())

    def test_is_safe_move_to(self):
        self.element.bomb_threat = None

        self.element.type = Element.EMPTY_SPACE
        self.assertTrue(self.element.is_safe_move_to())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertTrue(self.element.is_safe_move_to())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertTrue(self.element.is_safe_move_to())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.bomb_threat = Element(Element.TIMER_1_LEFT_BOMB, 0, 0)

        self.element.type = Element.EMPTY_SPACE
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_safe_move_to())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_safe_move_to())

    def test_is_possible_move_to(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertTrue(self.element.is_possible_move_to())

        self.element.type = Element.BREAKABLE_WALL
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertTrue(self.element.is_possible_move_to())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertTrue(self.element.is_possible_move_to())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.BOMB_FIRE
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_A
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_B
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_C
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_D
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_A_DIED
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_B_DIED
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_C_DIED
        self.assertFalse(self.element.is_possible_move_to())

        self.element.type = Element.PLAYER_D_DIED
        self.assertFalse(self.element.is_possible_move_to())

    def test_is_possible_trace_route(self):
        self.element.type = Element.EMPTY_SPACE
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.BREAKABLE_WALL
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.SOLID_WALL
        self.assertFalse(self.element.is_possible_trace_route())

        self.element.type = Element.FIRE_BOMB_POWER
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.EXTRA_BOMB_POWER
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.TIMER_2_LEFT_BOMB
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.TIMER_1_LEFT_BOMB
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.BOMB_FIRE
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_A
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_B
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_C
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_D
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_A_DIED
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_B_DIED
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_C_DIED
        self.assertTrue(self.element.is_possible_trace_route())

        self.element.type = Element.PLAYER_D_DIED
        self.assertTrue(self.element.is_possible_trace_route())

    # String representation
    def test__repr__(self):
        self.element.parent = None
        self.assertEquals(self.element.__repr__(), "Type: _ X: 0 Y: 0 Effort: 4 Move Effort: 2000 Parent: None")
        self.element.parent = Element(Element.EMPTY_SPACE, 1, 2)
        self.assertEquals(self.element.__repr__(), "Type: _ X: 0 Y: 0 Effort: 4 Move Effort: 2000 Parent: "
                                                   "[Type: _ X: 1 Y: 2]")