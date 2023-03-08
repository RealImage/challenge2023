""" Problem Statement 1

- Given a list of purchases, each has an item and its quantity.
- Find the vendor for each purchase where cost is minimum (primary objective) and time-efficient (secondary objective).  Do not assign multiple vendors to a single purchase.
- If a purchase is not possible, mark that purchase as not possible.
- Quantity will always be in KG.
- Use the data given in `vendors.csv`.

**Input**: A CSV file `input.csv`. Each row contains the purchase id, item, and required quantity.

**Expected Output**: A CSV file `output.csv`. Each row contains the purchase id, item, required quantity, indication if a purchase is possible (true/false), vendor, total cost, and delivery time.
"""

import pandas as pd
df = pd.read_csv("C:/Users/3108p/code_challenge/vendors.csv")

from flask import Flask, request, jsonify
app = Flask(__name__)

purchases = []
result = []

@app.route("/purchases", methods=["GET"])
def get_purchase():
    return jsonify(purchases)

@app.route("/purchases", methods=["POST"])
def computing_result():
    result_dictionary={}
    if request.is_json:
        purchase = request.get_json()
        purchases.append(purchase)
        cost = 1000000
        mintime = 10000
        isavail = "false"
        vendor = " "
        total = 0
        time = 0
        for j in range(df.shape[0]):
            
            if purchase["item"] == df["Item"][j]:
                
                if df["Cost Per KG"][j] < cost:
                    cost = int(df["Cost Per KG"][j])
                    mintime = int(df["Time to Deliver"][j])
                    isavail = "true"
                    vendor = df["Vendor"][j]
                    total = int(df["Cost Per KG"][j])*int(purchase["Req. Quantity"])
                    time = mintime
                
                elif int(df["Cost Per KG"][j]) == cost:
                
                    if int(df["Time to Deliver"][j]) < mintime:
                    
                        mintime = int(df["Time to Deliver"][j])
                        isavail = "true"
                        vendor = df["Vendor"][j]
                        total = int(df["Cost Per KG"][j])*int(purchase["Req. Quantity"])
                        time = mintime
                        
        result_dictionary["Purchase Id"] = purchase["Pur_id"]
        result_dictionary["Item"] = purchase["item"]
        result_dictionary["Quantity"] = purchase["Req. Quantity"]
        result_dictionary["IsAvail"] = isavail
        result_dictionary["Vendor"] = vendor
        result_dictionary["Total cost"] = total
        result_dictionary["Time"] = time
        result.append(result_dictionary)
        return result_dictionary,201
    return {"error": "Request must be JSON"}, 415

@app.route("/results", methods=["GET"])
def get_result():
    return jsonify(result)