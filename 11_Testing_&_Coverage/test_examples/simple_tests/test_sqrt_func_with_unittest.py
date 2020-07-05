import unittest

from sqrt_func_with_doctest import sqrt


class TestSqrt(unittest.TestCase):

    def test_square_root_of_9_positive(self):
        self.assertEqual(sqrt(9), 3.0)

    def test_square_root_of_negative(self):
        with self.assertRaises(ValueError) as e:
            sqrt(0)

        self.assertEqual(e.exception.args[0], 'Positive value required')


if __name__ == '__main__':
    unittest.main()
