import pandas as pd

def load_orders():

    return pd.read_csv("datasets/orders.csv")

def load_products():

    return pd.read_csv("datasets/products.csv")

def load_customers():

    return pd.read_csv("datasets/customers.csv")