class OnlineShop:
    """onlineshop that will help you to buy food online and finds you at your place"""

    def __init__(self):

        self.menu = {
            "Burger" : 1500.0,
            "Pizza" : 11750.0,
            "Coffee" : 2000.00,
            "Zigege": 150.0,
            "Sandwich": 2310.0,
            "Ice Cream" : 1220.0
        }

        self.orders = []

    def displayMenu(self):

        print("Onlineshop menu: ")
        for item,price in self.menu.items():
             print(f"{item} : MWK{price:2f}")

    def take_order(self):
        while True:
            self.displayMenu()
            order = input("Enter the item you want to order(type 'done' when you finish your orders): ").title()
            if order.lower() == 'done':
                break
            if order in self.menu:
                self.orders.append(order)
                print(f"{order} added to your order.")
            else:
                print("Sorry that item is not on the menu.")

    def display_orders(self):
        if not self.orders:
            print("you have not ordered anything yet.")
        else:
            print("your order:")
            for item in self.orders:
                print(f"- {item}")


    def checkout(self):
        if not self.orders:
            print("You have not ordered anything yet.")

        else:
            total = sum(self.menu[item] for item in self.orders)
            print(f"you have ordered {self.orders}")
            print(f"Your total is :MWK{total:2f}")
            payment = float(input("enter your payment amount: MWK"))
            if payment >= total:
                change = payment - total
                print(f"Thank you for your payment your change is MWK{change}")
            else:
                print("insufficeint payment .Please check out again.")



def main():
    onlineshop = OnlineShop()
    while True:
        print("\nWelcome to onlineshop")
        print("1.Display menu")
        print("2.Place order")
        print("3.Display order")
        print("4.Checkout")
        print("5.Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            onlineshop.displayMenu()
        elif choice == "2":
            onlineshop.take_order()
        elif choice == "3":
            onlineshop.display_orders()
        elif choice == "4":
            onlineshop.checkout()
        elif choice == "5":
            print("Thank you for visiting our shop.")
            break
        else:
            print("Invalid choice.Please try again.")

if __name__ == "__main__":
    main()