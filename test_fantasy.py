import unittest

from main import calc_actual_withdrawal


class TestFantasyLeague(unittest.TestCase):

    def test_withdraw_100(self):
        self.assertEqual(
            calc_actual_withdrawal(100),
            90.0
        )

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            calc_actual_withdrawal(-100)


if __name__ == "__main__":
    unittest.main()