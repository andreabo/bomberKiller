__author__ = 'Fredy Garcia, Carol Bohorquez'

from bomberkiller.elements.element import Element


class Rules:

    def __init__(self):
        self.players_bomb_magnitude = \
            {
                Element.PLAYER_A: 1,
                Element.PLAYER_B: 1,
                Element.PLAYER_C: 1,
                Element.PLAYER_D: 1
            }
        self.players_bombs_quantity = \
            {
                Element.PLAYER_A: 1,
                Element.PLAYER_B: 1,
                Element.PLAYER_C: 1,
                Element.PLAYER_D: 1
            }

    # It is not possible know who put the bomb
    def retrieve_max_bomb_magnitude(self, possible_players):
        # Ensure at least one 1 for list
        bomb_magnitude = [1]
        for player in possible_players:
            bomb_magnitude.append(self.players_bomb_magnitude[player.type])
        return max(bomb_magnitude)

    def retrieve_bombs_quantity(self, player):
        return self.players_bombs_quantity[player.type]

    def increase_bomb_magnitude(self, player):
        self.players_bomb_magnitude[player.type] += 1

    def increase_bombs_quantity(self, player):
        self.players_bombs_quantity[player.type] += 1
