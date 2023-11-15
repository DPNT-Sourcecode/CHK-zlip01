def checkout(sku_string: str) -> int:
    basket_map = {}
    for sku in sku_string:
        if sku in basket_map:
            basket_map[sku] += 1
        else:
            basket_map[sku] = 1
    

