from flask import Flask
from flask import render_template

from recommendation import recommend_products
from sales_analysis import sales_summary
from retention_analysis import retention_rate
from inventory_forecast import low_stock_products

from api import api

app = Flask(__name__)

app.register_blueprint(api)

@app.route("/")
def dashboard():

    sales = sales_summary()

    retention = retention_rate()

    stock = low_stock_products()

    recommendations = recommend_products(1)

    return render_template(

        "dashboard.html",

        sales=sales,

        retention=retention,

        stock=stock,

        recommendations=recommendations
    )

if __name__ == "__main__":

    app.run(debug=True)