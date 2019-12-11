import unittest

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.Validator = PassValidator("JONES")


    def test_space(self):
        space = self.validator.space("J O N E S")
        self.assertEqual(space, "J O N E S")

    def test_upper(self):
        self.assertEqual('jones'.upper(), 'JoNES')

    def test_isupper(self):
        self.assertTrue('JONES'.isupper())
        self.assertFalse('jones'.isupper())

    def test_isnotnum(self):
        self. assertEqual('JONES'. character(), 'JONES')

    def test_isnopunctation(self):
        self.


