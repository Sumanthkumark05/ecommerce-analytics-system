from database import load_orders

def customer_behavior():

    orders = load_orders()

    behavior = orders.groupby(
        "CustomerID"
    )["Quantity"].sum()

    return behavior.to_dict()