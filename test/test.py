__author__ = 'Fredy Garcia, Carol Bohorquez'

import unittest
from pymock.pymock import PyMockTestCase


class TestKillerMock(PyMockTestCase):

    def test_method(self):
        m = self.mock()
        self.expectAndReturn(m.getSomething("And"), 3)
        self.expectAndReturn(m.getSomething("Or"), 5)
        self.replay()
        #self.failUnless(m.getSomething("And") == 3)
        print m.getSomething("And")
        print m.getSomething("Or")
        #print m.getSomething("Otherwise")
        self.verify()


class TestKiller(unittest.TestCase):
    def set_up(self):
        self.seq = range(10)

    def test_something(self):
        pass

    # def test_shuffle(self):
    #
    #     # make sure the shuffled sequence does not lose any elements
    #     random.shuffle(self.seq)
    #     self.seq.sort()
    #     self.assertEqual(self.seq, range(10))
    #
    #     # should raise an exception for an immutable sequence
    #     self.assertRaises(TypeError, random.shuffle, (1, 2, 3))
    #
    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)
    #
    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()

#| X,X,X,X,X,X,X,X,X,X,X |
#| X,_,_,_,_,_,_,_,_,_,X |
#| X,_,X,L,X,_,X,L,X,_,X |
#| X,_,L,D,_,_,_,L,L,L,X |
#| X,_,X,_,X,_,X,_,X,_,X |
#| X,_,_,_,_,_,_,_,_,_,X |
#| X,_,X,_,X,_,X,_,X,_,X |
#| X,_,L,L,_,_,_,_,L,_,X |
#| X,_,X,L,X,_,X,L,X,_,X |
#| X,_,_,L,_,_,_,L,_,_,X |
#| X,X,X,X,X,X,X,X,X,X,X |