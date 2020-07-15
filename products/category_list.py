def unique_category_list(products_list):
    category_list = []

    for product in products_list:
        if product.category not in category_list:
            category_list.append(product.category)

    return category_list