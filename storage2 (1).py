products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]


def print_products():
    for i, product in enumerate(products, start=1):
        print(f"{i}, Název produktu2: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Cena produktu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)

def search_product():
    question = input("Zadejte název produktu:"),
    answer = [p for p in products if question in p["name"]]
    if answer:
        for products in answer:
            print(f"Název produktu: {products[name]} Cena produktu: {product[price]}$")
    else:
        print("Žádný produkt jsme nenašli.")

def total_price():
    total = sum(p["price"] for p in products)
    print(f"Celková cena: {total}$")

def max_price():
    max = max(p["price"] for p in products)
    most_expensive = [p for p in products if p["price"] == max]
    for products in most_expensive:
        print(f"Nejdražší produkt: {products[name]}; Cena produktu: {products[price]}$")

def min_price():
    min = min(p["price"] for p in products)
    cheapest_product = [p for p in products if p["price"] == min]
    for products in cheapest_product:
        print(f"Nejlevnější produkt: {products[name]}; Cena produktu: {products[price]}$")

def average_price():
    average = sum(p["price"] for p in products)
    print(f"Průměrná cena: {average:2f}$")

def edit_product():
    print_products()
    index = int(input("Zadej číslo produktu, který bys chtěl upravovat: "))-1
    if 0 <= index < len(products):
        products[index]["name"] = input("Upravený název produktu:")
        products[index]["price"] = float(input("Upravená cena produktu:"))
        print("Produkt byl upraven")
    else:
        print("Produkt nebyl upraven")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky\n")
    print("3. Vyhledáváí produktu\n")
    print("4. Celková cena produktů\n")
    print("5. Nejdražší produkt\n")
    print("6. Nejlevnější produkt\n")
    print("7. Průměrná cena produktu\n")
    print("8. Úprava produktu\n")
    print("9. Konec\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledaný produkt:")
        print_products()
        print("")
        menu()

    elif choice == 4:
        print("Celková cena produktu:")
        print_products()
        print("")
        menu()

    elif choice == 5:
        print("Nejdražší produkt:")
        print_products()
        print("")
        menu()

    elif choice == 6:
        print("Nejlevnější produkt:")
        print_products()
        print("")
        menu()

    elif choice == 7:
        print("Průměrná cena produktu:")
        print_products()
        print("")
        menu()

    elif choice == 8:
        print("Upravený produkt:")
        print_products()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
