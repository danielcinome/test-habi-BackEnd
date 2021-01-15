""" Test Display """
import unittest

from display import Display
from display import validate_lines

class testDisplay(unittest.TestCase):
    """Test for methods in class display
    """

    # TEST NUMBERS
    def test_print_size1(self):
        dispaly = Display('number')
        num_cero = dispaly.print(1, '0')
        num_one = dispaly.print(1, '1')
        num_two = dispaly.print(1, '2')
        num_three = dispaly.print(1, '3')
        num_four = dispaly.print(1, '4')
        num_five = dispaly.print(1, '5')
        num_six = dispaly.print(1, '6')
        num_seven = dispaly.print(1, '7')
        num_eight = dispaly.print(1, '8')
        num_nine = dispaly.print(1, '9')

        self.assertEqual(num_cero,  ' - \n| |\n   \n| |\n - \n')
        self.assertEqual(num_one,   '   \n  |\n   \n  |\n   \n')
        self.assertEqual(num_two,   ' - \n  |\n - \n|  \n - \n')
        self.assertEqual(num_three, ' - \n  |\n - \n  |\n - \n')
        self.assertEqual(num_four,  '   \n| |\n - \n  |\n   \n')
        self.assertEqual(num_five,  ' - \n|  \n - \n  |\n - \n')
        self.assertEqual(num_six,   ' - \n|  \n - \n| |\n - \n')
        self.assertEqual(num_seven, ' - \n  |\n   \n  |\n   \n')
        self.assertEqual(num_eight, ' - \n| |\n - \n| |\n - \n')
        self.assertEqual(num_nine,  ' - \n| |\n - \n  |\n - \n')

    def test_print_size3(self):
        dispaly = Display('number')
        num_cero = dispaly.print(3, '0')
        num_one = dispaly.print(3, '1')
        num_two = dispaly.print(3, '2')
        num_three = dispaly.print(3, '3')
        num_four = dispaly.print(3, '4')
        num_five = dispaly.print(3, '5')
        num_six = dispaly.print(3, '6')
        num_seven = dispaly.print(3, '7')
        num_eight = dispaly.print(3, '8')
        num_nine = dispaly.print(3, '9')

        self.assertEqual(num_cero,  ' --- \n|   |\n|   |\n|   |\n     \n|   |\n|   |\n|   |\n --- \n')
        self.assertEqual(num_one,   '     \n    |\n    |\n    |\n     \n    |\n    |\n    |\n     \n')
        self.assertEqual(num_two,   ' --- \n    |\n    |\n    |\n --- \n|    \n|    \n|    \n --- \n')
        self.assertEqual(num_three, ' --- \n    |\n    |\n    |\n --- \n    |\n    |\n    |\n --- \n')
        self.assertEqual(num_four,  '     \n|   |\n|   |\n|   |\n --- \n    |\n    |\n    |\n     \n')
        self.assertEqual(num_five,  ' --- \n|    \n|    \n|    \n --- \n    |\n    |\n    |\n --- \n')
        self.assertEqual(num_six,   ' --- \n|    \n|    \n|    \n --- \n|   |\n|   |\n|   |\n --- \n')
        self.assertEqual(num_seven, ' --- \n    |\n    |\n    |\n     \n    |\n    |\n    |\n     \n')
        self.assertEqual(num_eight, ' --- \n|   |\n|   |\n|   |\n --- \n|   |\n|   |\n|   |\n --- \n')
        self.assertEqual(num_nine,  ' --- \n|   |\n|   |\n|   |\n --- \n    |\n    |\n    |\n --- \n')

    def test_horizontal(self):
        dispaly = Display('number')
        horizontal = dispaly.horizontal(1, 4, 0)
        self.assertEqual(horizontal,  ' ---- ')

        horizontal = dispaly.horizontal(0, 0, 4)
        self.assertEqual(horizontal,  '    ')

    def test_vertical(self):
        dispaly = Display('number')
        vertical = dispaly.vertical(1, 5)
        self.assertEqual(vertical,  '      |')

        vertical = dispaly.vertical(2, 5)
        self.assertEqual(vertical,  '|      ')

        vertical = dispaly.vertical(3, 5)
        self.assertEqual(vertical,  '|     |')



if __name__ == '__main__':
    unittest.main()