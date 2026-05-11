from database import load_orders

def retention_rate():

    orders = load_orders()

    repeat_customers = orders[
        orders.duplicated(
            subset=["CustomerID"],
            keep=False
        )
    ]["CustomerID"].nunique()

    total_customers = orders["CustomerID"].nunique()

    rate = (
        repeat_customers /
        total_customers
    ) * 100

    return round(rate, 2)