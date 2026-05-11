from flask import Blueprint, jsonify

from sales_analysis import sales_summary

api = Blueprint("api", __name__)

@api.route("/sales-api")
def sales_api():

    return jsonify(
        sales_summary()
    )