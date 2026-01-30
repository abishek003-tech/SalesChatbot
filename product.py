# =====================================
# Sales Chatbot using Switch-Case
# With Product Number Selection
# =====================================

PRODUCTS = {
    1: {"name": "Laptop", "price": 55000, "stock": 5},
    2: {"name": "Mobile", "price": 20000, "stock": 10},
    3: {"name": "Headphones", "price": 1500, "stock": 25},
    4: {"name": "Keyboard", "price": 800, "stock": 15},
    5: {"name": "Mouse", "price": 500, "stock": 20},
    6: {"name": "Monitor", "price": 12000, "stock": 8},
    7: {"name": "Printer", "price": 9000, "stock": 6},
    8: {"name": "Speaker", "price": 3000, "stock": 12},
    9: {"name": "Webcam", "price": 2500, "stock": 10},
    10: {"name": "Router", "price": 1800, "stock": 14}
}


def display_products():
    print("\n📦 Available Electronic Products")
    print("-" * 60)
    print(f"{'S.No':<6}{'Product':<15}{'Price (₹)':<15}{'Stock'}")
    print("-" * 60)

    for sno, item in PRODUCTS.items():
        print(f"{sno:<6}{item['name']:<15}{item['price']:<15}{item['stock']}")

    print("-" * 60)


def buy_product():
    try:
        choice = int(input("👉 Enter product S.No: "))
    except ValueError:
        print("🤖 Please enter a valid number.")
        return

    match choice:
        case choice if choice in PRODUCTS:
            product = PRODUCTS[choice]

            if product["stock"] == 0:
                print("🤖 Sorry, product is out of stock.")
                return

            try:
                qty = int(input(f"👉 How many {product['name']} do you want? "))
            except ValueError:
                print("🤖 Invalid quantity.")
                return

            if qty <= 0:
                print("🤖 Quantity must be greater than zero.")
                return

            if qty > product["stock"]:
                print(f"🤖 Only {product['stock']} items available.")
                return

            total = qty * product["price"]
            product["stock"] -= qty

            print("\n🧾 BILL")
            print("-" * 30)
            print(f"Product  : {product['name']}")
            print(f"Quantity : {qty}")
            print(f"Total    : ₹{total}")
            print("-" * 30)
            print("🤖 Purchase Successful ✅")

        case _:
            print("🤖 Invalid product number.")


def start_chatbot():
    print("🤖 Welcome to ABC Electronics Store")
    print("🤖 I am your Sales Assistant\n")

    while True:
        print("\nCommands:")
        print("  1 → View available products")
        print("  2 → Buy a product")
        print("  3 → Exit")

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
                buy_product()
            case 3:
                print("🤖 Thank you for shopping 😊")
                break
            case _:
                print("🤖 Invalid option. Try again.")


# Run chatbot
start_chatbot()
