# noinspection PyShadowingBuiltins,PyUnusedLocal

class Basket:
    def __init__(self, sku_items: str):
        self.sku_values = {
            "A": 50, "B": 30,
            "C": 20, "D": 15,
            "E": 40, "F": 10,
            "G": 20, "H": 10,
            "I": 35, "J": 60,
            "K": 70, "L": 90,
            "M": 15, "N": 40,
            "O": 10, "P": 50,
            "Q": 30, "R": 50,
            "S": 20, "T": 20,
            "U": 40, "V": 50,
            "W": 20, "X": 17,
            "Y": 20, "Z": 21
        }

        self.sku_offers = {
            "A": [(5, 200), (3, 130)], "B": [(2, 45)],
            "H": [(5, 45), (10, 80)], "K": [(2, 120)],
            "P": [(5, 200)], "Q": [(3, 80)],
            "V": [(2, 90), (3, 130)]
        }

        self.reductive_offers = {
            "E": [(2, ("B", 1))], "F": [(2, ("F", 1))],
            "N": [(3, ("M", 1))], "R": [(3, ("Q", 1))],
            "U": [(3, ("U", 1))]
        }

        self.group_offers = {"S", "T", "X", "Y", "Z"}

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

        basket_total, basket_map = self._applyGroupOffers(basket_map)

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
        for reductive_sku in self.reductive_offers:
            if reductive_sku in basket_map:
                best_reductive_offers = sorted(self.reductive_offers[reductive_sku], key=lambda x: x[0], reverse=True)

                for required_freq, offer in best_reductive_offers:
                    if required_freq <= basket_map[reductive_sku]:
                        applied_sku, reduction = offer
                        if applied_sku not in basket_map:
                            continue

                        if applied_sku == reductive_sku:
                            reduction = (
                                    basket_map[applied_sku] //
                                    (required_freq + reduction)
                            )
                        else:
                            reduction = basket_map[reductive_sku] // required_freq

                        basket_map[applied_sku] -= reduction

        return basket_map

    def _applyGroupOffers(self, basket_map):
        groups_in_basket = []
        for sku, freq in basket_map:
            if sku in self.group_offers:
                groups_in_basket.append((sku, freq, self.sku_values[sku]))

        if len(groups_in_basket) < 3:
            return basket_map

        groups_in_basket.sort(key=lambda x: x[2], reverse=True)



        return basket_map

    def getValue(self):
        return self.basket_value


def checkout(sku_string: str) -> int:
    basket = Basket(sku_string)
    return basket.getValue()

