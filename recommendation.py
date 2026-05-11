from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from database import load_orders

def recommend_products(customer_id):

    orders = load_orders()

    pivot = orders.pivot_table(
        index="CustomerID",
        columns="ProductID",
        values="Quantity",
        fill_value=0
    )

    similarity = cosine_similarity(pivot)

    similarity_df = pd.DataFrame(
        similarity,
        index=pivot.index,
        columns=pivot.index
    )

    similar_users = similarity_df[customer_id].sort_values(
        ascending=False
    )

    recommended = similar_users.index[1:4]

    return list(recommended)