from database import load_products

def low_stock_products():

    products = load_products()

    low_stock = products[
        products["Stock"] < 20
    ]

    return low_stock.to_dict(
        orient="records"
    )