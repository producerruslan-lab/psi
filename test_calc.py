# test_calc.py
import unittest

from calc import usage

class TestCalc(unittest.TestCase):
    def test_usage_exists(self):
        # просто проверяем, что функция объявлена
        self.assertTrue(callable(usage))

if __name__ == "__main__":
    unittest.main(verbosity=2)
