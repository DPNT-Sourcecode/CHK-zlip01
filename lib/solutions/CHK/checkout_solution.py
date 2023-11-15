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
            "E": [(2, (-self.sku_values["B"])]

        }

        self.basket_value = self._calculateBasketValue(sku_items)

    def _calculateBasketValue(self, sku_items):
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

        basket_total = 0

        for sku_identifier, frequency in basket_map.items():
            if sku_identifier in self.sku_offers:
                basket_total += self._calculateSkuOffer(sku_identifier, frequency)
            else:
                basket_total += self.sku_values[sku_identifier] * frequency

        return basket_total

    def _calculateSkuOffer(self, currSKU, currFreq):
        total_offer = 0
        best_sku_offers = sorted(self.sku_offers[currSKU], key=lambda x: x[0], reverse=True)

        for offer_frequency, offer_value in best_sku_offers:
            if offer_frequency > currFreq:
                total_offer += (currFreq // offer_frequency) * offer_value
                currFreq %= offer_frequency
            if currFreq == 0:
                break

        if currFreq > 0:
            total_offer += self.sku_values[currSKU]

        return total_offer

    def getValue(self):
        return self.basket_value


def checkout(sku_string: str) -> int:
    basket = Basket(sku_string)
    return basket.getValue()








