from main import soma
import unittest


class TestMain(unittest.TestCase):
    def test_soma_pass(self):
        self.assertEqual(soma(1, 2), 3)

    def test_soma_error(self):
        self.assertNotEqual(soma(1, 2), 2)
