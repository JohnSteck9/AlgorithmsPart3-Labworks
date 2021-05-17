import unittest
from Rabin_Karp import *


class TestCareer(unittest.TestCase):
    def test_find_max_experience1(self):
        self.assertEqual(main("Some text here", "re"), True)
        self.assertEqual(main("Some text here", " text"), True)
        self.assertEqual(main("Some text here", "S"), True)


if __name__ == "__main__":
    unittest.main()
