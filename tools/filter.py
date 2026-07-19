def filter_by_budget(products, budget):
    return [product for product in products if float(product["price"][1:]) <= budget]


if __name__ == "__main__":
    pass