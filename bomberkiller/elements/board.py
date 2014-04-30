__author__ = 'Fredy Garcia, Carol Bohorquez'

from bomberkiller.elements.element import Element
from bomberkiller.game.action import Action


class Board:

    def __init__(self):
        self.elements = []

        self.bomber_killer = None
        self.enemies = []
        self.powers = []
        self.bombs = []

    def retrieve_element_by_position(self, x, y):
        if 0 <= x <= 10 and 0 <= y <= 10:
            return self.elements[y][x]

    def retrieve_element(self, element_base, action=None):
        if action == Action.EAST:
            return self.retrieve_element_by_position(element_base.x + 1, element_base.y)
        elif action == Action.WEST:
            return self.retrieve_element_by_position(element_base.x - 1, element_base.y)
        elif action == Action.NORTH:
            return self.retrieve_element_by_position(element_base.x, element_base.y - 1)
        elif action == Action.SOUTH:
            return self.retrieve_element_by_position(element_base.x, element_base.y + 1)
        else:
            return self.retrieve_element_by_position(element_base.x, element_base.y)

    def retrieve_contiguous_elements(self, element_base):
        elements = []
        directions = \
            [
                Action.EAST,
                Action.WEST,
                Action.NORTH,
                Action.SOUTH
            ]
        for direction in directions:
            cell = self.retrieve_element(element_base, direction)
            if cell is not None:
                elements.append(cell)
        return elements

    def __repr__(self):
        rows = []
        for i, row in enumerate(self.elements):
            columns = []
            for k, col in enumerate(row):
                if col.type == Element.EMPTY_SPACE:
                    if col.bomb_threat is not None:
                        if col.bomb_threat.type == Element.TIMER_2_LEFT_BOMB:
                            columns.append("*")
                        elif col.bomb_threat.type == Element.TIMER_1_LEFT_BOMB:
                            columns.append("$")
                        else:
                            columns.append("?")
                    else:
                        columns.append(" ")
                elif col.type == Element.BREAKABLE_WALL:
                    columns.append("W")
                else:
                    columns.append(col.type)
            rows.append('| %s |' % ".".join(columns))

        return '\n'.join(rows)