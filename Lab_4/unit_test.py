import unittest
from ijones import *

FILE_IN_1 = 'data/ijones1.in'
FILE_IN_2 = 'data/ijones2.in'
FILE_IN_3 = 'data/ijones3.in'


class TestCareer(unittest.TestCase):
    def test_find_max_experience1(self):
        self.assertEqual(main(FILE_IN_1), 5)

    def test_find_max_experience2(self):
        self.assertEqual(main(FILE_IN_2), 2)

    def test_find_max_experience3(self):
        self.assertEqual(main(FILE_IN_3), 201684)


if __name__ == "__main__":
    unittest.main()
