import unittest

from greeting import greet


class TestGreet(unittest.TestCase):
    def test_named_greeting(self):
        self.assertEqual(greet("Ada"), "Hi, Ada!")

    def test_name_unchanged(self):
        self.assertEqual(greet("  Ada  "), "Hi,   Ada  !")
        self.assertEqual(greet(""), "Hi, !")


if __name__ == "__main__":
    unittest.main()
