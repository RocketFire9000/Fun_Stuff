total_cost = 0.00
quantity = 0
tax_rate = 1.1
products = ["bread", "flour", "sugar", "milk", "pay"]
price = [2.15, 2.38, 3.99, 4.19, None]
purchase = input("Please input the item you wish to purchase, or 'pay' to pay for your purchases:")
while purchase.lower() != "pay":
    if purchase.lower() in products:
        quantity = input("How many would you like to purchase?")
        total_cost += (price[products.index(purchase.lower())] * int(quantity))
        purchase = input("Please input the item you wish to purchase, or 'pay' to end the purchase:")
    else:
        print("That item is not available. Please select another.")
        purchase = input("Please input the item you wish to purchase, or 'pay' to end the purchase:")
no_tax = total_cost
total_cost *= tax_rate
print("Your final price is: $" + "%.2f" % total_cost)
print("Tax amount: $" + "%.2f" % (total_cost - no_tax))
# TODO; add a bank system with another program, or maybe a file.
