import unittest

def sum(num_1, num_2):
    return abs(num_1) + num_2

class black_box_test(unittest.TestCase):

    def test_sum_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = sum(num_1, num_2)

        self.assertEqual(result, 15)

    def test_sum_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = sum(num_1, num_2)

        self.assertEqual(result, -17)  

if __name__ == "__main__":
    unittest.main()      