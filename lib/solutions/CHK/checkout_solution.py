def checkout(sku_string: str) -> int:
    
    # Get the frequency of all the unique SKU identifiers
    # in the basket, to be able to calculate the total
    # basket value efficiently 

    basket_map = {}
    for sku in sku_string:
        if sku in basket_map:
            basket_map[sku] += 1
        else:
            basket_map[sku] = 1
    
    # Maps the SKU identifiers to their values

    value_map = {}
    

    basket_total = 0

    for sku_identifier, frequency in basket_map.items():
        if sku_identifier != "A" and sk

