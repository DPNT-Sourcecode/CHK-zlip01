from unittest import TestCase
from lib.solutions.CHK.checkout_solution import checkout


class CheckoutTests(TestCase):
    def test_chk_single_item(self):
        self.assertEqual(checkout('A'), 50)

    def test_chk_multiple_items(self):
        self.assertEqual(checkout('ABCD'), 115)

    def test_chk_offer_items(self):
        self.assertEqual(checkout('AAABCD'), 195)

    def test_chk_invalid_items(self):
        self.assertEqual(checkout('R'), -1)

    def test_chk_no_items(self):
        self.assertEqual(checkout(''), 0)

    def test_chk_combo_items(self):
        self.assertEqual(checkout('AAAAAA'), 250)

    def test_chk_lowerCase_item(self):
        self.assertEqual(checkout('ABCd'), -1)

