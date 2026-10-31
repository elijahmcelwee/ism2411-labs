def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")
print()


def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")
print()


discounted = apply_discount(200, "gold")
with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${with_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')
print()


orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
print()


# A variable created at the top level of the file is global, so the whole
# file can see it. A variable assigned inside a function is local: it only
# exists while that function runs, even if it shares a name with a global.
# The x = 999 inside double_it() is a separate local x, so the global x
# stays 100 before and after the call.
x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
