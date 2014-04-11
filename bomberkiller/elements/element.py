__author__ = 'Fredy Garcia, Carol Bohorquez'


class Element(object):

    EMPTY_SPACE = "_"

    BREAKABLE_WALL = "L"
    SOLID_WALL = "X"

    FIRE_BOMB_POWER = "P"
    EXTRA_BOMB_POWER = "V"

    TIMER_2_LEFT_BOMB = "2"
    TIMER_1_LEFT_BOMB = "1"

    BOMB_FIRE = "#"

    PLAYER_A = "A"
    PLAYER_B = "B"
    PLAYER_C = "C"
    PLAYER_D = "D"

    PLAYER_A_DIED = "a"
    PLAYER_B_DIED = "b"
    PLAYER_C_DIED = "c"
    PLAYER_D_DIED = "d"

    def __init__(self, type, x, y):
        # Type of cell
        self.type = type
        # X position in board
        self.x = x
        # Y position in board
        self.y = y
        # Bomb threat
        self.bomb_threat = None
        # Individual effort to reach this element
        self.individual_effort = 0
        # Effort of all movement in the board starting from bomber killer position to reach this element
        self.move_effort = 2000
        # Parent cell based in the path to bomber killer after calculate the best path
        self.parent = None
        # Calculate individual effort to reach this element
        self.reset_individual_effort()

    def change_type(self, type):
        self.type = type
        self.reset_individual_effort()

    # Calculate the effort to move to this element
    def reset_individual_effort(self):
        if self.type == Element.EMPTY_SPACE:
            # Standard effort
            self.individual_effort = 4
        elif self.type == Element.BREAKABLE_WALL:
            # Breakable wall is 4 times normal effort, but is decreased by the possibility to found some power
            self.individual_effort = 10
        elif self.type == Element.SOLID_WALL:
            # Effort is infinite because is not possible pass over solid wall
            self.individual_effort = 9999
        elif self.type == Element.FIRE_BOMB_POWER:
            # Effort decreased in order to get a power
            self.individual_effort = 1
        elif self.type == Element.EXTRA_BOMB_POWER:
            # Effort decreased in order to get a power
            self.individual_effort = 1
        elif self.type == Element.TIMER_2_LEFT_BOMB:
            # Rik increased by exposure to a bomb which explode in three times
            self.individual_effort = 30
        elif self.type == Element.TIMER_1_LEFT_BOMB:
            # Rik increased even more by exposure to a bomb which explode in two times
            self.individual_effort = 50
        elif self.type == Element.BOMB_FIRE:
            # Although a exploded bomb should not be a risk in the next turn, the server does not allow move
            self.individual_effort = 80
        elif self.type == Element.PLAYER_A:
            # Effort decreased in order to try kill a player
            self.individual_effort = 2
        elif self.type == Element.PLAYER_B:
            # Effort decrease in order to try kill a player
            self.individual_effort = 2
        elif self.type == Element.PLAYER_C:
            # Effort decrease in order to try kill a player
            self.individual_effort = 2
        elif self.type == Element.PLAYER_D:
            # Effort decrease in order to try kill a player
            self.individual_effort = 2
        elif self.type == Element.PLAYER_A_DIED:
            # A died player neither is a risk nor is an incentive anymore
            self.individual_effort = 4
        elif self.type == Element.PLAYER_B_DIED:
            # A died player neither is a risk nor is an incentive anymore
            self.individual_effort = 4
        elif self.type == Element.PLAYER_C_DIED:
            # A died player neither is a risk nor is an incentive anymore
            self.individual_effort = 4
        elif self.type == Element.PLAYER_D_DIED:
            # A died player neither is a risk nor is an incentive anymore
            self.individual_effort = 4

    # Increase effort with specified value
    def increase_effort(self, effort):
        self.individual_effort += effort

    def is_bomb_range(self):
        return self.bomb_threat is not None

    def is_empty_space(self):
        return self.type == Element.EMPTY_SPACE

    def is_breakable_wall(self):
        return self.type == Element.BREAKABLE_WALL

    def is_solid_wall(self):
        return self.type == Element.SOLID_WALL

    def is_wall(self):
        return self.is_breakable_wall() or self.is_solid_wall()

    def is_power(self):
        return self.type == Element.FIRE_BOMB_POWER or self.type == Element.EXTRA_BOMB_POWER

    def is_bomb(self):
        return self.type == Element.TIMER_2_LEFT_BOMB \
            or self.type == Element.TIMER_1_LEFT_BOMB

    def is_bomb_fire(self):
        return self.type == Element.BOMB_FIRE

    def is_alive_player(self):
        return self.type == Element.PLAYER_A \
            or self.type == Element.PLAYER_B \
            or self.type == Element.PLAYER_C \
            or self.type == Element.PLAYER_D

    def is_player(self):
        return self.type == Element.PLAYER_A \
            or self.type == Element.PLAYER_B \
            or self.type == Element.PLAYER_C \
            or self.type == Element.PLAYER_D \
            or self.type == Element.PLAYER_A_DIED \
            or self.type == Element.PLAYER_B_DIED \
            or self.type == Element.PLAYER_C_DIED \
            or self.type == Element.PLAYER_D_DIED

    # Is safe move if bomber killer does not have risk to die
    def is_safe_move_to(self):
        return self.is_possible_move_to() and not self.is_bomb_range()

    # Is possible move us to this cell or place a bomb there
    def is_possible_move_to(self):
        return self.is_empty_space() \
            or self.is_power()

    # Is not possible trace route over solid walls
    def is_possible_trace_route(self):
        return self.is_empty_space() \
            or self.is_power() \
            or self.is_bomb() \
            or self.is_bomb_fire() \
            or self.is_player() \
            or self.is_breakable_wall()

    # String representation
    def __repr__(self):
        string = "Type: " + self.type + " X: " + str(self.x) + " Y: " + str(self.y) + \
            " Effort: " + str(self.individual_effort) + " Move Effort: " + str(self.move_effort) + " Parent: "
        if self.parent is None:
            string += "None"
        else:
            string += "[Type: " + self.parent.type + " X: " + str(self.parent.x) + " Y: " + str(self.parent.y) + "]"
        return string
