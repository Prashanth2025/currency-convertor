# from flask import Flask, request, jsonify
# import requests
# from dotenv import load_dotenv
# import os

# # Load .env variables
# load_dotenv()
# API_KEY = os.getenv("EXCHANGE_API_KEY")

# app = Flask(__name__)

# @app.route('/convert', methods=['GET'])
# def convert_currency():
#     amount = request.args.get('amount', type=float)
#     currency = request.args.get('currency')

#     if not amount or not currency:
#         return jsonify({"error": "Missing required parameters"}), 400

#     url = f"https://api.exchangerate-api.com/v4/latest/USD"
#     response = requests.get(url)

#     if response.status_code != 200:
#         return jsonify({"error": "Failed to fetch exchange rates"}), 500

#     data = response.json()
#     rates = data.get("rates", {})

#     if currency not in rates:
#         return jsonify({"error": "Invalid currency code"}), 400

#     converted_amount = amount * rates[currency]
    
#     return jsonify({"converted_amount": converted_amount, "currency": currency})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os
from flask_cors import CORS

# Load environment variables
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

@app.route('/convert', methods=['POST'])  # Change to POST
def convert_currency():
    data = request.get_json()  # Get JSON data from request

    amount = data.get("amount")
    currency = data.get("currency")

    if not amount or not currency:
        return jsonify({"error": "Missing required parameters"}), 400

    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exchange rates"}), 500

    data = response.json()
    rates = data.get("rates", {})

    if currency not in rates:
        return jsonify({"error": "Invalid currency code"}), 400

    converted_amount = amount * rates[currency]
    
    return jsonify({"converted_amount": converted_amount, "currency": currency})

if __name__ == '__main__':
    app.run(debug=True)
