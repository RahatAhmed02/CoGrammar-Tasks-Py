# List of menu items defined
menu = ["Cappuccino", "Avocado Toast", "Blueberry Muffins", "Caesar Salad", "Vegetarian Panini", "Chocolate Croissant"]

# Dictionary that stores the stock quantity for each menu item defined
stock = {
    "Cappuccino": 45,
    "Avocado Toast": 25,
    "Blueberry Muffins": 30,
    "Caesar Salad": 15,
    "Vegetarian Panini": 20,
    "Chocolate Croissant": 35,
}

# Dictionary that stores the price for each menu item defined
price = {
    "Cappuccino": 3.5,
    "Avocado Toast": 5,
    "Blueberry Muffins": 2.5,
    "Caesar Salad": 4,
    "Vegetarian Panini": 3,
    "Chocolate Croissant": 3,
}

# Variable to keep track of the total stock value intialised
total_stock = 0

# Each menu item iterated through
for key in menu:
    # The value of the total items calculated by multiplication of the stock quantity by the item's price
    items_value = stock[key] * price[key]
    # Add the value of the current menu item to the total stock value
    total_stock += items_value

# Print the total value of all items in stock
print(f"Total stock value: £{total_stock:.2f}")
