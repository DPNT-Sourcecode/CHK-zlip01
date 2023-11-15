# noinspection PyShadowingBuiltins,PyUnusedLocal

class Basket:
    def __init__(self, sku_items: str):
        self.sku_values = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }

        self.sku_offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "E": [(2, self.sku_values["B"])]

        }

        self.basket_value = self._calulateBasketValue(sku_items)

    def _calulateBasketValue(self, sku_items):
        if sku_items == "":
            return 0

        # Get the frequency of all the unique SKU identifiers
        # in the basket, to be able to calculate the total
        # basket value efficiently

        basket_map = {}

        for sku_identifier in sku_items:
            # Not Valid SKU
            if sku_identifier not in self.sku_values.keys():
                return -1
            if sku_identifier in basket_map:
                basket_map[sku_identifier] += 1
            else:
                basket_map[sku_identifier] = 1

        # Maps the SKU identifiers to their values
        value_map = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }

        basket_total = 0

        for sku_identifier, frequency in basket_map.items():
            if sku_identifier == "A":
                if frequency >= 3:
                    basket_total += (frequency // 3) * 130
                    frequency = frequency % 3
            elif sku_identifier == "B":
                if frequency >= 2:
                    basket_total += (frequency // 2) * 45
                    frequency = frequency % 2

            basket_total += frequency * value_map[sku_identifier]

        return basket_total

    def getValue(self):
        return self.basket_value


def checkout(sku_string: str) -> int:
    basket = Basket(sku_string)
    return basket.getValue()
