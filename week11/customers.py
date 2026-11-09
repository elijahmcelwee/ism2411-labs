# ISM2411 Lab 11 — Customer Dictionary & Lookup


# ---------------------------------------------------------------
# Exercise 1: One customer
# ---------------------------------------------------------------
print("=== Exercise 1: One customer ===")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}

# Print each field using key access
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

# Print the whole dict
print(customer)
print()


# ---------------------------------------------------------------
# Exercise 2: Update and add
# ---------------------------------------------------------------
print("=== Exercise 2: Update and add ===")

# Add a phone field
customer["phone"] = "555-123-4567"
print("After adding phone:", customer)

# Update the tier
customer["tier"] = "platinum"
print("After updating tier:", customer)

# Delete the email field
del customer["email"]
print("After deleting email:", customer)
print()


# ---------------------------------------------------------------
# Exercise 3: Safe lookup
# ---------------------------------------------------------------
print("=== Exercise 3: Safe lookup ===")

# .get() returns the default instead of crashing when the key is missing
email = customer.get("email", "no email on file")
print("Using .get():", email)

# Bracket notation raises a KeyError when the key is missing
try:
    email = customer["email"]
    print("Using brackets:", email)
except KeyError as error:
    print("Using brackets: KeyError raised for", error)
print()


# ---------------------------------------------------------------
# Exercise 4: Iterate
# ---------------------------------------------------------------
print("=== Exercise 4: Iterate ===")

# .items() gives both the key and the value on each pass
for key, value in customer.items():
    print(f"{key}: {value}")

print("--- without .items() ---")

# Looping over a dict directly gives only the KEYS, not the values.
# To get each value, you have to look it up yourself with customer[key].
# .items() hands you the key and value together as a pair, so no lookup is needed.
for key in customer:
    print(f"{key}: {customer[key]}")
print()


# ---------------------------------------------------------------
# Exercise 5: Lookup table
# ---------------------------------------------------------------
print("=== Exercise 5: Lookup table ===")

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {tier}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price on ${purchase}: ${final_price:.2f}")
print()


# ---------------------------------------------------------------
# Exercise 6: List of dicts
# ---------------------------------------------------------------
print("=== Exercise 6: List of dicts ===")

customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 1250.00},
    {"name": "Ben", "tier": "silver", "ytd_spend": 430.50},
    {"name": "Carla", "tier": "bronze", "ytd_spend": 85.00},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']:<6} | tier: {c['tier']:<8} | discount on ${purchase}: ${discount_amount:.2f}")
print()


# ---------------------------------------------------------------
# Exercise 7: Nested catalog
# ---------------------------------------------------------------
print("=== Exercise 7: Nested catalog ===")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} has only {details['stock']} left")
print()


# ---------------------------------------------------------------
# Exercise 8: Sales by region
# ---------------------------------------------------------------
print("=== Exercise 8: Sales by region ===")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    region = t["region"]
    # .get(region, 0) starts a new region at 0, then we add this amount
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
