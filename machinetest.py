def calculate_total_price(order):
    total_price = 0
    for product in order:
        quantity = order[product]['quantity']
        price = order[product]['price']
        total_price += quantity * price
    return total_price

def apply_discount_rules(order, total_price):
    discounts = {
        'flat_10_discount': {'threshold': 200, 'discount': 10},
        'bulk_5_discount': {'threshold': 10, 'discount': 5},
        'bulk_10_discount': {'threshold': 20, 'discount': 10},
        'tiered_50_discount': {'threshold': 30, 'discount': 50}
    }

    applicable_discounts = {}
    
    if total_price > discounts['flat_10_discount']['threshold']:
        applicable_discounts['flat_10_discount'] = discounts['flat_10_discount']['discount']
    
    for product in order:
        quantity = order[product]['quantity']
        if quantity > discounts['bulk_5_discount']['threshold']:
            applicable_discounts['bulk_5_discount'] = discounts['bulk_5_discount']['discount']
            break
    
    total_quantity = sum(order[product]['quantity'] for product in order)
    if total_quantity > discounts['bulk_10_discount']['threshold']:
        applicable_discounts['bulk_10_discount'] = discounts['bulk_10_discount']['discount']
    
    for product in order:
        quantity = order[product]['quantity']
        if quantity > discounts['tiered_50_discount']['threshold']:
            applicable_discounts['tiered_50_discount'] = discounts['tiered_50_discount']['discount']
            break
    
    max_discount = 0.0
    discount_name = ''
    for name, discount in applicable_discounts.items():
        if discount > max_discount:
            max_discount = discount
            discount_name = name
    
    return max_discount, discount_name

def calculate_shipping_fee(total_quantity):
    package_count = total_quantity // 10
    if total_quantity % 10 != 0:
        package_count += 1
    shipping_fee = package_count * 5
    return shipping_fee

def calculate_gift_wrap_fee(order):
    gift_wrap_fee = 0
    for product in order:
        quantity = order[product]['quantity']
        if order[product]['gift_wrap']:
            gift_wrap_fee += quantity
    return gift_wrap_fee

products = {
    'productA': {'name': 'Product A', 'price': 20.0},
    'productB': {'name': 'Product B', 'price': 40.0},
    'productC': {'name': 'Product C', 'price': 50.0}
}

order = {}

for product in products:
    quantity = int(input(f"Enter the total quantity of {products[product]['name']}: "))
    gift_wrap = input(f"Is {products[product]['name']} do you want to wrap as a gift? (y/n): ")
    gift_wrap = True if gift_wrap.lower() == 'y' else False
    order[product] = {'quantity': quantity, 'price': products[product]['price'], 'gift_wrap': gift_wrap}

total_price = calculate_total_price(order)

discount_amount, discount_name = apply_discount_rules(order, total_price)
discounted_price = total_price - (total_price * discount_amount / 100)

total_quantity = sum(order[product]['quantity'] for product in order)
shipping_fee = calculate_shipping_fee(total_quantity)

gift_wrap_fee = calculate_gift_wrap_fee(order)

subtotal = discounted_price + gift_wrap_fee

total = subtotal + shipping_fee

print("Product\t\tQuantity\tTotal")
for product in order:
    name = products[product]['name']
    quantity = order[product]['quantity']
    total_amount = order[product]['price'] * quantity
    print(f"{name}\t\t{quantity}\t\t${total_amount:.2f}")
print("-------------------------------")
print(f"Subtotal:\t\t\t${subtotal:.2f}")
if discount_name:
    print(f"{discount_name} Discount:\t-{discount_amount}%")
print(f"Shipping Fee:\t\t\t${shipping_fee:.2f}")
print(f"Gift Wrap Fee:\t\t\t${gift_wrap_fee:.2f}")
print("-------------------------------")
print(f"Total:\t\t\t\t${total:.2f}")
