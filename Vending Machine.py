class VendingMachine:
    def __init__(self):
        #products in the vending machine
        self.products = {
            'A1': {'name': 'Soft Drinks', 'category': 'Drinks', 'price': 3.00, 'quantity': 10},
            'A2': {'name': 'Water', 'category': 'Drinks', 'price': 1.00, 'quantity': 15},
            'B1': {'name': 'Chips', 'category': 'Snacks', 'price': 2.50, 'quantity': 20},
            'B2': {'name': 'Chocolate', 'category': 'Snacks', 'price': 4.75, 'quantity': 12},
            'C1': {'name': 'Biscuit', 'category': 'Snacks', 'price': 3.25, 'quantity': 40},
            'C1': {'name': 'Jelly', 'category': 'Snacks', 'price': 2.00, 'quantity': 8},
        }
        self.money_inserted = 0
#display the product, their category and amount.
    def display_products(self):
        print("Welcome!")
        print("Available products are:")
        for code, product in self.products.items():
            print(f"{code}: {product['name']} - AED{product['price']} - Category: {product['category']} - Quantity: {product['quantity']}")

    def select_product(self, code):
        if code in self.products:
            return self.products[code]
        else:
            return None

    def insert_money(self, amount):
        self.money_inserted += amount

    def purchase(self, product):
        if product['quantity'] > 0 and self.money_inserted >= product['price']:
            print(f"You've purchased {product['name']}.")
            product['quantity'] -= 1
            change = self.money_inserted - product['price']
            if change > 0:
                print(f"Your change: AED{change:.2f}")
            self.money_inserted = 0
        else:
            if product['quantity'] <= 0:
                print("Sorry, this item is not in stock anymore.")
            else:
                print("Insufficient payment.")
#suggestions for more of the stuff from the vending machine of the same category
    def suggest_purchase(self, category):
        suggestions = [prod['name'] for code, prod in self.products.items() if prod['category'] == category]
        if suggestions:
            print(f"If you like {category}, might I suggest: {', '.join(suggestions)}")
#function calling
def main():
    vending_machine = VendingMachine()
    vending_machine.display_products()

#while loop to quit or purchase more items
    while True:
        choice = input("Enter the code of the product (or 'q' to quit): ")
        if choice.lower() == 'q':
            break

        product = vending_machine.select_product(choice)
        if product:
            vending_machine.insert_money(float(input("Enter the amount: AED")))
            vending_machine.purchase(product)
            vending_machine.suggest_purchase(product['category'])

    print("Thank you for using the vending machine,Enjoy!")


