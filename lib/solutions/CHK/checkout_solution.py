# noinspection PyShadowingBuiltins,PyUnusedLocal
def checkout(sku_string: str) -> int:
    if sku_string == "" : return 0
    
    
    valid_sku_identifiers = set(['A', 'B', 'C', 'D'])
    sku_string = sku_string.upper()

    # Get the frequency of all the unique SKU identifiers
    # in the basket, to be able to calculate the total
    # basket value efficiently 
    
    basket_map = {}
    
    for sku_identifier in sku_string:
        if sku_identifier not in valid_sku_identifiers:
            return -1
        if sku_identifier in basket_map:
            basket_map[sku_identifier] += 1
        else:
            basket_map[sku_identifier] = 1
    
    # Maps the SKU identifiers to their values
    value_map = {
        "A" : 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    basket_total = 0

    for sku_identifier, frequency in basket_map.items():
        if sku_identifier == "A":
            if frequency >= 3:
                basket_total += 130
                frequency -= 3
        elif sku_identifier == "B":
            if frequency >= 2:
                basket_total += 45
                frequency -= 2
       
        basket_total += frequency * value_map[sku_identifier]
    
    return basket_total

    