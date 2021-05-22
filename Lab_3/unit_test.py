import unittest
from main import *


class TestCareer1(unittest.TestCase):
    def test_find_max_experience1(self):
        career_1 = Career()
        career_1.layers_num = 4
        career_1.layers_list = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(career_1.find_max_experience(), 16)

    def test_find_max_experience2(self):
        career_2 = Career()
        career_2.layers_num = 4
        career_2.layers_list = [[4], [3, 1], [2, 1, 5], [1, 3, 2, 1]]
        self.assertEqual(career_2.find_max_experience(), 12)

    def test_find_max_experience3(self):
        career_3 = Career()
        career_3.layers_num = 1
        career_3.layers_list = [[9999]]
        self.assertEqual(career_3.find_max_experience(), 9999)

    def test_find_max_experience4(self):
        career_4 = Career()
        career_4.layers_num = 5
        career_4.layers_list = [[0], [1, 1], [0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1, 0]]
        self.assertEqual(career_4.find_max_experience(), 3)


if __name__ == "__main__":
    unittest.main()
