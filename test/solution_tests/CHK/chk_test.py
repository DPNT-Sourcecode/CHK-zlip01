from unittest import TestCase
from lib.solutions.CHK.checkout_solution import checkout


class CheckoutTests(TestCase):
    def test_chk_single_item(self):
        self.assertEqual(checkout('A'), 50)

    def test_chk_two_item(self):
        self.assertEqual(100, checkout('AA'))

    def test_chk_four_item(self):
        self.assertEqual(180, checkout('AAAA'))

    def test_chk_multiple_items(self):
        self.assertEqual(checkout('ABCD'), 115)

    def test_chk_offer_items(self):
        self.assertEqual(checkout('AAA'), 130)

    def test_chk_invalid_items(self):
        self.assertEqual(checkout('x'), -1)

    def test_chk_no_items(self):
        self.assertEqual(checkout(''), 0)

    def test_chk_combo_items(self):
        self.assertEqual( checkout('AAAAA'), 200)

    def test_chk_lowerCase_item(self):
        self.assertEqual(-1, checkout('ABCd'), )

    def test_chk_multiple_combo_items(self):
        self.assertEqual(130 + 80, checkout('AAABEE'))

    def test_chk_getFFree(self):
        self.assertEqual(checkout('FFFFFF'), 40)

    def test_chk_multiple_reductions(self):
        self.assertEqual(checkout('BEEFFF'),80 + 20)

    def test_chk_reductive_combo_offer(self):
        self.assertEqual(checkout('EEEEBB'), 160)

    def test_chk_reductive_combo_offer_2(self):
        self.assertEqual(checkout('AAAMMNNNNNNRRR'),
                         130 + (6 * 40) + 150)

    def test_chk_group_offer_1(self):
        self.assertEqual(checkout('STX'), 45)

    def test_chk_group_offer_2(self):
        self.assertEqual(checkout('STXSTX'), 90)

    def test_chk_group_offer_3(self):
        self.assertEqual(checkout('XXSTZ'), 45 + (17 * 2))

    def test_chk_group_offer_4(self):
        self.assertEqual(checkout('SSS'), 45)





