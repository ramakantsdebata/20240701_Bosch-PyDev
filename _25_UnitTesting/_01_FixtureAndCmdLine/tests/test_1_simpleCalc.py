import unittest

import sys
sys.path.insert(0, '..\\')
from _25_UnitTesting._01_FixtureAndCmdLine.src.simpleCalculator import Calculator


class TestSimpleCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass...")
        cls.calc = Calculator(0, 0)

    def setUp(self):
        print("In setUp...")
        self.calc.a = 7
        self.calc.b = 4

    def tearDown(self):
        print("In tearDown...")
        self.calc.a = 0
        self.calc.b = 0

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass...")
        del cls.calc

    @parameterized([

    ])
    def test_simpleAdd(self):

        self.assertEqual(11, self.calc.add())  # add assertion here

    def test_simpleSub(self):
        self.assertEqual(3, self.calc.sub())  # add assertion here

    def test_simpleAdd2(self):
        self.assertEqual(3, self.calc.add2(1, 1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
