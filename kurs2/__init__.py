import unittest
def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass

class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        x = int
        self.assertEqual(x, 'string')
        self.assertEqual(x, 1.5)
'''
    def test_negative(self):
        pass

    def test_zero_and_one_cases(self):
        pass

    def test_simple_numbers(self):
        pass

    def test_two_simple_multipliers(self):
        pass

    def test_many_multipliers(self):
        pass
'''

if __name__ == "__main__":
    unittest.main()