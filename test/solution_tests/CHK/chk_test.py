from unittest import TestCase
from solutions.CHK.checkout_solution import checkout

class CheckoutTests(TestCase):
    def chk_single_item(self):
        self.assertEqual(checkout('A'), 50)

    def chk_multiple_items(self):
        self.assertEqual(checkout('ABCD'), 115)

    def chk_offer_items(self):
        self.assertEqual(checkout('AAABCD'), 195)

    def chk_invalid_items(self):
        self.assertEqual(checkout('R'), -1)