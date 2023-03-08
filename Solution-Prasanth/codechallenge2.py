"""

We have provided `vendor_capacities.csv` which contains vendor, item, cost, delivery time, quantity limit, and additional cost.

- Given a list of purchases, each has an item and its quantity.
- Find the vendor for each purchase where cost is minimum (primary objective) and time-efficient (secondary objective).  Do not assign multiple vendors to a single purchase.
- Consider the quantity limit and additional cost if a purchase quantity exceeds the quantity limit. If a purchase is not possible, mark that purchase impossible.
- Quantity will always be in KG.
- Use the data given in `vendor_capacities.csv`.

**Input**: A CSV file input-capacities.csv. Each row contains the purchase id, item, and required quantity.

**Expected Output**: Same as Problem statement 1.

"""

import pandas as pd
df = pd.read_csv("C:/Users/3108p/code_challenge/vendor-capacities.csv")

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
        mincost = 100000
        mintime = 1000
        isavail = "false"
        vendor = " "
        for j in range(df.shape[0]):
            
            if purchase["item"] == df["Item"][j]:
                
                if int(df["Default Quantity Limit in KG"][j]) >= int(purchase["Req. Quantity"]):
                    
                    cost = int(df["Cost Per KG"][j])*int(purchase["Req. Quantity"])
                
                else:
                
                    additional = int(df["Cost Per KG"][j]) + int(df["Additional Cost Per KG"][j])
                    addtocost = ((int(purchase["Req. Quantity"])-int(df["Default Quantity Limit in KG"][j])) * additional)
                    cost = (int(df["Cost Per KG"][j]) * int(df["Default Quantity Limit in KG"][j])) + addtocost
            
                if cost < mincost: 
                    mincost = int(cost)
                    mintime = int(df["Time to Deliver"][j])
                    isavail = "true"
                    vendor = df["Vendor"][j]
                    
                elif cost == mincost:
                    
                    if df["Time to Deliver"][j] < mintime:
                        
                        mintime = int(df["Time to Deliver"][j])
                        isavail = "true"
                        vendor = df["Vendor"][j]
                        
        result_dictionary["Purchase Id"] = purchase["Pur_id"]
        result_dictionary["Item"] = purchase["item"]
        result_dictionary["Quantity"] = purchase["Req. Quantity"]
        result_dictionary["IsAvail"] = isavail
        result_dictionary["Vendor"] = vendor
        if mincost == 100000 and mintime == 1000:
            total=0
            time=0
        else:
            total=mincost
            time=mintime
        result_dictionary["Total cost"] = total
        result_dictionary["Time"] = time
        result.append(result_dictionary)
        return result_dictionary,201
    return {"error": "Request must be JSON"}, 415

@app.route("/results", methods=["GET"])
def get_result():
    return jsonify(result)