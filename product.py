# =====================================
# Grocery Shop Chatbot
# 30 Items with Cart System
# =====================================

PRODUCTS = {
    1: {"name": "Apple (Red)", "price": 180, "stock": 50, "unit": "kg"},
    2: {"name": "Banana", "price": 60, "stock": 100, "unit": "doz"},
    3: {"name": "Milk (1L)", "price": 65, "stock": 40, "unit": "pkt"},
    4: {"name": "Bread (Brown)", "price": 45, "stock": 30, "unit": "pkt"},
    5: {"name": "Eggs (6pcs)", "price": 50, "stock": 60, "unit": "box"},
    6: {"name": "Potato", "price": 30, "stock": 80, "unit": "kg"},
    7: {"name": "Onion", "price": 40, "stock": 70, "unit": "kg"},
    8: {"name": "Tomato", "price": 25, "stock": 90, "unit": "kg"},
    9: {"name": "Rice (Basmati)", "price": 120, "stock": 100, "unit": "kg"},
    10: {"name": "Wheat Flour (5kg)", "price": 250, "stock": 25, "unit": "bag"},
    11: {"name": "Sugar (1kg)", "price": 45, "stock": 50, "unit": "kg"},
    12: {"name": "Salt (1kg)", "price": 20, "stock": 100, "unit": "pkt"},
    13: {"name": "Cooking Oil (1L)", "price": 160, "stock": 40, "unit": "btl"},
    14: {"name": "Tea Powder (250g)", "price": 150, "stock": 35, "unit": "pkt"},
    15: {"name": "Coffee (100g)", "price": 280, "stock": 20, "unit": "jar"},
    16: {"name": "Butter (100g)", "price": 55, "stock": 45, "unit": "pkt"},
    17: {"name": "Cheese Slices", "price": 140, "stock": 30, "unit": "pkt"},
    18: {"name": "Yogurt (500g)", "price": 60, "stock": 20, "unit": "cup"},
    19: {"name": "Paneer (200g)", "price": 90, "stock": 25, "unit": "pkt"},
    20: {"name": "Chicken (1kg)", "price": 240, "stock": 15, "unit": "kg"},
    21: {"name": "Carrot", "price": 50, "stock": 40, "unit": "kg"},
    22: {"name": "Spinach", "price": 20, "stock": 30, "unit": "bunch"},
    23: {"name": "Garlic (250g)", "price": 40, "stock": 50, "unit": "pkt"},
    24: {"name": "Ginger (250g)", "price": 35, "stock": 50, "unit": "pkt"},
    25: {"name": "Green Chilies (100g)", "price": 15, "stock": 100, "unit": "pkt"},
    26: {"name": "Detergent (1kg)", "price": 190, "stock": 30, "unit": "pkt"},
    27: {"name": "Dish Soap", "price": 50, "stock": 40, "unit": "btl"},
    28: {"name": "Shampoo (200ml)", "price": 180, "stock": 25, "unit": "btl"},
    29: {"name": "Toothpaste", "price": 95, "stock": 50, "unit": "tube"},
    30: {"name": "Soap (Pack of 3)", "price": 120, "stock": 40, "unit": "box"}
}

CART = []

def display_products():
    print("\n🛒 Available Grocery Items")
    print("-" * 70)
    print(f"{'S.No':<6}{'Item':<25}{'Price (₹)':<15}{'Unit':<10}{'Stock'}")
    print("-" * 70)

    for sno, item in PRODUCTS.items():
        print(f"{sno:<6}{item['name']:<25}{item['price']:<15}{item['unit']:<10}{item['stock']}")

    print("-" * 70)

def add_to_cart():
    try:
        choice = int(input("👉 Enter item S.No to add to cart: "))
    except ValueError:
        print("🤖 Please enter a valid number.")
        return

    if choice not in PRODUCTS:
        print("🤖 Invalid product number.")
        return

    product = PRODUCTS[choice]
    if product["stock"] <= 0:
        print(f"🤖 Sorry, {product['name']} is out of stock.")
        return

    try:
        qty = int(input(f"👉 How many units of {product['name']} ({product['unit']})? "))
    except ValueError:
        print("🤖 Invalid quantity.")
        return

    if qty <= 0:
        print("🤖 Quantity must be greater than zero.")
        return

    if qty > product["stock"]:
        print(f"🤖 Only {product['stock']} units available.")
        return

    # Add to cart
    total_item_price = qty * product["price"]
    CART.append({
        "sno": choice,
        "name": product["name"],
        "qty": qty,
        "price": product["price"],
        "total": total_item_price,
        "unit": product["unit"]
    })
    
    product["stock"] -= qty
    print(f"✅ Added {qty} {product['unit']} of {product['name']} to cart.")

def view_cart_and_checkout():
    if not CART:
        print("🤖 Your cart is empty.")
        return

    print("\n🛒 YOUR CART")
    print("-" * 60)
    print(f"{'Item':<25}{'Qty':<10}{'Price':<10}{'Total (₹)'}")
    print("-" * 60)
    
    grand_total = 0
    for item in CART:
        print(f"{item['name']:<25}{item['qty']:<10}{item['price']:<10}{item['total']}")
        grand_total += item["total"]

    print("-" * 60)
    print(f"{'GRAND TOTAL':<45}₹{grand_total}")
    print("-" * 60)

    confirm = input("👉 Confim purchase? (y/n): ").lower()
    if confirm == 'y':
        print("\n🧾 FINAL BILL GENERATED")
        print("🤖 Thank you for your purchase! ✅")
        CART.clear()
    else:
        print("🤖 Keeping items in cart for now.")

def start_chatbot():
    print("🤖 Welcome to Super Grocery Mart")
    print("🤖 I am your Shopping Assistant\n")

    while True:
        print("\nCommands:")
        print("  1 → View available items")
        print("  2 → Add item to cart")
        print("  3 → View cart & Checkout")
        print("  4 → Exit")

        try:
            command = int(input("You: "))
        except ValueError:
            print("🤖 Please enter a valid option.")
            continue

        match command:
            case 1:
                display_products()
            case 2:
                display_products()
                add_to_cart()
            case 3:
                view_cart_and_checkout()
            case 4:
                if CART:
                    print("🤖 Your cart has items. Are you sure you want to leave?")
                    check = input("(y/n): ").lower()
                    if check != 'y': continue
                print("🤖 Thank you for visiting! Have a great day 😊")
                break
            case _:
                print("🤖 Invalid option. Try again.")

if __name__ == "__main__":
    start_chatbot()

