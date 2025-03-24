products = [
    {"name": "Audi", "price": 50},
    {"name": "BMW", "price": 30}
]


def print_products():
    for i, product in enumerate(products, start=1):
        print(f"{i}. Název: {product['name']}, Cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu: ")
    product_price = float(input("Cena produktu: "))
    products.append({"name": product_name, "price": product_price})
    print("Produkt byl přidán.")


def search_product():
    question = input("Zadejte název produktu: ").lower()
    found_products = [p for p in products if question in p["name"].lower()]

    if found_products:
        for product in found_products:
            print(f"Název: {product['name']}, Cena: {product['price']}$")
    else:
        print("Žádný produkt jsme nenašli.")


def total_price():
    total = sum(p["price"] for p in products)
    print(f"Celková cena: {total}$")


def max_price():
    max_price = max(p["price"] for p in products)
    expensive_products = [p for p in products if p["price"] == max_price]

    for product in expensive_products:
        print(f"Nejdražší produkt: {product['name']}, Cena: {product['price']}$")


def min_price():
    min_price = min(p["price"] for p in products)
    cheapest_products = [p for p in products if p["price"] == min_price]

    for product in cheapest_products:
        print(f"Nejlevnější produkt: {product['name']}, Cena: {product['price']}$")


def average_price():
    avg = sum(p["price"] for p in products) / len(products)
    print(f"Průměrná cena: {avg:.2f}$")


def edit_product():
    print_products()
    index = int(input("Zadejte číslo produktu k úpravě: ")) - 1

    if 0 <= index < len(products):
        products[index]["name"] = input("Nový název: ")
        products[index]["price"] = float(input("Nová cena: "))
        print("Produkt byl upraven.")
    else:
        print("Neplatná volba.")


def menu():
    while True:
        print("\nVítejte ve skladu")
        print("################")
        print("1. Výpis položek")
        print("2. Přidání položky")
        print("3. Vyhledávání produktu")
        print("4. Celková cena produktů")
        print("5. Nejdražší produkt")
        print("6. Nejlevnější produkt")
        print("7. Průměrná cena produktu")
        print("8. Úprava produktu")
        print("9. Konec")

        choice = input("Zadejte volbu: ")

        if choice == "1":
            print_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            total_price()
        elif choice == "5":
            max_price()
        elif choice == "6":
            min_price()
        elif choice == "7":
            average_price()
        elif choice == "8":
            edit_product()
        elif choice == "9":
            print("Děkujeme za použití programu!")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


menu()
