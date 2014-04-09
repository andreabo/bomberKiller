__author__ = 'frealgagu'

import unittest


class StrategyTest(unittest.TestCase):

    def test_move_or_put_a_bomb(self):
        pass

# Poderes: {'A': 2, 'C': 1, 'B': 1, 'D': 1} . {'A': 1, 'C': 1, 'B': 2, 'D': 1}
# Mapa actual:
# | X.X.X.X.X.X.X.X.X.X.X |
# | X. . . . .*.A.2.*.*.X |
# | X. .X.W.X. .X.W.X.B.X |
# | X. .W.W.W.C.W.W.W.$.X |
# | X. .X. .X. .X. .X.1.X |
# | X. . . . . . . .D.$.X |
# | X. .X. .X. .X. .X. .X |
# | X. .W.W.W. .W.W. . .X |
# | X. .X.W.X. .X.W.X. .X |
# | X. . .W. . . .W. . .X |
# | X.X.X.X.X.X.X.X.X.X.X |
