# Qube Cinema - Campus Challenge 2023

Bob owns a fruits and vegetable shop. He is struggling to find cost-effective and time-efficient vendors to buy the items required to meet his demand.

You are going to help Bob to solve his problem. And, your solution will be helpful for many shop owners like Bob.

Vendors specify the cost of each item in the following manner:  
Note: All costs are in Rupees and time taken to deliver is specified in minutes.

Table 1:

| Vendor        | Item         |  Cost Per KG  | Time to Deliver |
| ------------- |:------------:|:-------------:|:---------------:|
|  V1           |  Banana      |       200     | 120             |
|  V2           |  Banana      |       190     | 60              |
|  V1           |  Broccoli     |       160     | 120             |
|  V1           |  Apple       |       500     | 120             |
|  V3           |  Orange      |       200     | 120             |
|  V3           |  Tomato      |       20      | 30              |
|  V4           |  Tomato      |       20      | 60              |

- Vendor V1 supplies bananas at the cost of 200 rupees per kg. However, Vendor V2 supplies the same at 190 rupees per kg and also delivers sooner than V1. Bob would prefer to buy bananas from Vendor V2.
- For tomatoes, Bob will prefer vendor V3 over V4, because V3 can deliver in 30 minutes whereas V4 will take 60 minutes.
- Bob always prefers cost-effective vendors and considers delivery time as a second factor.

*NOTE*:

- Write program in any language you want. Feel free to hold the datasets in whatever data structure you want, but try not to use external databases as far as possible. Stick to your language without bringing in MySQL/Postgres/MongoDB/Redis/SQLite Etc.
- The data in the Readme is just an example. We've provided a CSV `vendors.csv` with the list of all vendors, items, cost per kgs, and time to deliver. Please use the data mentioned in `vendors.csv` for your program instead of the data given in the sample data tables.
- This challenge consists of two problems. Aim to solve at least Problem Statement 1.

## Problem Statement 1

- Given a list of purchases, each has an item and its quantity.
- Find the vendor for each purchase where cost is minimum (primary objective) and time-efficient (secondary objective).
- If a purchase is not possible, mark that purchase as not possible.
- Quantity will always be in KG.
- Use the data given in `vendors.csv`.

**Input**: A CSV file `input.csv`. Each row contains the purchase id, item, and required quantity.

**Expected Output**: A CSV file `output.csv`. Each row contains the purchase id, item, required quantity, indication if a purchase is possible (true/false), vendor, total cost, and delivery time.

#### Sample Scenarios (Based on above table 1):
**INPUT**:
```
P1, Banana,     10
P2, Apple,      20
P3, Watermelon, 50
```

**OUTPUT**:
```
P1, Banana,     10, true,  V2,    1900,    60
P2, Apple,      20, true,  V1,   10000,   120
P3, Watermelon, 50, false,   ,       0,     0
```

---

**INPUT**:
```
P1, Banana,     10
P2, Tomato,     8
```

**OUTPUT**:
```
P1, Banana,     10, true,  V2,   1900,   60
P2, Tomato,      8, true,  V3,    160,   30
```

---

## Problem Statement 2

Each vendor specifies the **default quantity limit in KG** they can serve, for each purchase. If a purchase quantity exceeds a given default quantity limit of a vendor, the vendor will charge an additional cost per KG in following manner:
  
Table 2:
| Vendor        | Item         |  Cost Per KG  | Time to Deliver | Default Quantity Limit in KG | Additional Cost Per KG |
| ------------- |:------------:|:-------------:|:---------------:|:--------------------:|:----------------------:|
|  V1           |  Banana      |       200     | 120             | 200                  | 5                      |
|  V2           |  Banana      |       190     | 60              | 50                   | 30                     |
|  V1           |  Broccoli     |       160     | 120             | 10                   | 10                     |
|  V1           |  Apple       |       500     | 120             | 10                   | 10                     |
|  V3           |  Orange      |       200     | 120             | 20                   | 10                     |
|  V3           |  Tomato      |       19      | 30              | 30                   | 11                     |
|  V4           |  Tomato      |       20      | 30              | 50                   | 5                      |
|  V5           |  Tomato      |       20      | 60              | 50                   | 5                      |

We have provided `vendor_capacities.csv` which contains vendor, item, cost, delivery time, quantity limit, and additional cost.

- Given a list of purchases, each has an item and its quantity.
- Find the vendor for each purchase where cost is minimum and time-efficient.
- Consider the quantity limit and additional cost if a purchase quantity exceeds the quantity limit. If a purchase is not possible, mark that purchase impossible.
- Quantity will always be in KG.
- Use the data given in `vendor_capacities.csv`.

**Input**: A CSV file input-capacities.csv. Each row contains the purchase id, item, and required quantity.

**Expected Output**: Same as Problem statement 1.

#### Sample Scenario (Based on above table 2):
**INPUT**:

```
P1, Banana,     100 
P2, Apple,      20
P3, Tomato,     100
P4, Watermelon, 50
```

**OUTPUT**:

```
P1, Banana,     100, true,  V1,   20000,    60
P2, Apple,      20,  true,  V1,   10000,   120
P3, Tomato,     100, true,  v4,   2250,     30
P4, Watermelon, 50,  false,   ,       0,      0
```

---

**INPUT**:

```
P1, Banana,     100
P2, Tomato,     100
```

**OUTPUT**:

```
P1, Banana,     100, true,  V1,   20000,   120
P2, Tomato,     100, true,  V4,    2250,   30
```

---

**Explanation**:

P1:

- Vendors V1 and V2 can supply bananas.
- Via V1: `(100*200) = 20000` in 120 mins
- Via V2: `((50*190) + (50*220)) = 20500` in 60 mins
- Buyers look for cost-effective and then delivery time. So, choosing V1.

P2:

- Vendors V3, V4 and V5 can supply tomatoes.
- Via V3: `((30*19) + (70*30)) = 2670` in 30 mins
- Via V4: `((50*20) + (50*25)) = 2250` in 30 mins
- Via V5: `((50*20) + (50*25)) = 2250` in 60 mins
- Buyers look for cost-effective and then delivery time. So, choosing V4 as V4 can deliver earlier than V5.

Note: Choose any vendors, if you find more than one vendor that can supply the demand at the same time, at the same cost.

To submit a solution, fork this repo and send a Pull Request on GitHub.

For any questions or clarifications, raise an issue on this repo and we'll answer your questions as fast as we can.
