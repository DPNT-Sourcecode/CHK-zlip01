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
        }
        self.reductive_offers = {
            "E": [(2, ("B", 1))]
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

        basket_map = self._applyReductiveOffers(basket_map)

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
            if offer_frequency <= currFreq:
                total_offer += (currFreq // offer_frequency) * offer_value
                currFreq %= offer_frequency

            if currFreq == 0:
                break

        if currFreq > 0:
            total_offer += self.sku_values[currSKU] * currFreq

        return total_offer

    def _applyReductiveOffers(self, basket_map):
        if "E" in basket_map:
            freq = basket_map["E"]
            if freq >= 2 and "B" in basket_map:
                basket_map["B"] -= freq // 2
        return basket_map

    def getValue(self):
        return self.basket_value


def checkout(sku_string: str) -> int:
    basket = Basket(sku_string)
    return basket.getValue()






