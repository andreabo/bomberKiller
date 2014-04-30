__author__ = 'Fredy Garcia, Carol Bohorquez'

from unittest import TestCase
from bomberkiller.game.action import Action


class TestAction(TestCase):

    def __init__(self, method_name=None):
        super(TestAction, self).__init__(method_name)

    def setUp(self):
        super(TestAction, self).setUp()
        self.action = Action()

    def tearDown(self):
        super(TestAction, self).tearDown()

    def test_action(self):
        pass