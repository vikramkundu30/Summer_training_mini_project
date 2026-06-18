cart = []
categories = set()
prices = {
    "Apple": 30,
    "Milk": 50,
    "Bread": 40,
    "Soap": 25
}
item_categories = {
    "Apple": "Fruits",
    "Milk": "Dairy",
    "Bread": "Bakery",
    "Soap": "Personal Care"
}
def add_item(item):
    if item in prices:
        cart.append(item)
        categories.add(item_categories[item])
        print(f"{item} added to cart.")
    else:
        print("Item not available.")

def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
        categories.clear()
        for i in cart:
            categories.add(item_categories[i])
    else:
        print("Item not in cart.")
def show_cart():
    print("\nCart Items:", cart)
    print("Unique Categories:", categories)
    total = 0
    for item in cart:
        total += prices[item]

    print("Total Bill: ₹", total)
add_item("Apple")
add_item("Milk")
add_item("Bread")

show_cart()

remove_item("Milk")

show_cart()
