# Reflection
# 1. [Your answer in 2-3 sentences: what surprised you about how lists work
#    in Python compared to what you expected.]
#
# 2. [Your answer in 2-3 sentences: a real business situation where a Python
#    list would have saved you time compared to doing it manually in Excel.]


# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
print()


# Exercise 2
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])
print()


# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])
print()


# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)
print()


# Exercise 5
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples can't be changed after they're created, which makes them a good fit")
    print("for coordinates: a location's latitude and longitude should never be")
    print("overwritten by accident somewhere else in the program.")
print(coords)
print()


# Exercise 6
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")
print()


# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(f"Original:   {prices}")
print(f"Discounted: {discounted}")
print()


# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
