from database import load_orders

def sales_summary():

    orders = load_orders()

    total_sales = (
        orders["Quantity"] *
        orders["Price"]
    ).sum()

    total_orders = len(orders)

    top_product = orders.groupby(
        "ProductName"
    )["Quantity"].sum().idxmax()

    return {

        "total_sales": round(total_sales, 2),
        "total_orders": total_orders,
        "top_product": top_product
    }