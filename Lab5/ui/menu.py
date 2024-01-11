from controller.controller import Controller

class UI:
    def __init__(self):
        self.controller = Controller()

    def run_2_0(self):
        while True:
            self.main_menu()

    def manage_customers(self):
        print('''

                       1. Add customer
                       2. Search for customer
                       3. Update a customers name
                       4. Search for a customer after his address  
                       5. Print all customers
                       6. Exit

                       ''')

        choice = int(input('Your choice: '))

        if choice == 1:
            customers = self.controller.return_all_customers()
            customer_ids = [customer.id for customer in customers]
            last_id_customers = max(customer_ids) + 1 if customer_ids else 1
            customer_name = input('Input the customers name: ')
            customer_address = input('Input the customers address: ')

            self.controller.add_customer(last_id_customers, customer_name, customer_address)

        elif choice == 2:
            part_name = input('Enter the name or partial name of the customer you would like to search: ')
            print(self.controller.search_for_customer(part_name))

        elif choice == 3:
            old_name = input('Enter the customers old name that you would like to update: ')
            new_name = input('Enter the customers new name: ')
            self.controller.update_customers_name(old_name, new_name)

        elif choice == 4:
            part_address = input(
                'Enter the full address or the partial address of the customer you would like to search: ')
            print(self.controller.search_for_customer_after_part_address(part_address))

        elif choice == 5:
            self.controller.print_customers()

        else:
            self.main_menu()

    def manage_menu(self):
        print('''

                       1. Manage cooked dishes
                       2. Manage drinks
                       3. Exit

                       ''')

        choice = int(input('Your choice: '))

        if choice == 1:
            self.manage_cooked_dishes()

        elif choice == 2:
            self.manage_drinks()

        else:
            self.main_menu()

    def manage_cooked_dishes(self):
        print('''

                           1. Add cooked dish
                           2. Show all cooked dishes by ID
                           3. Exit

                           ''')

        choice = int(input('Your choice: '))

        if choice == 1:
            cooked_dishes = self.controller.return_all_cooked_dishes()
            cooked_dishes_ids = [cooked_dish.id for cooked_dish in cooked_dishes]
            last_id_cooked_dishes = max(cooked_dishes_ids) + 1 if cooked_dishes_ids else 1
            cooked_dish_price = int(input('Enter the price of the cooked dish: '))
            cooked_dish_prep_time = int(input('Enter the preparation time of the cooked dish: '))
            cooked_dish_portion_size = 350

            self.controller.add_cooked_dish(last_id_cooked_dishes, cooked_dish_price, cooked_dish_prep_time,
                                            cooked_dish_portion_size)

        elif choice == 2:
            self.controller.print_cooked_dishes()

        else:
            self.manage_menu()

    def manage_drinks(self):
        print('''

                          1. Add drinks
                          2. Show all drinks by ID
                          3. Exit

                          ''')

        choice = int(input('Your choice: '))

        if choice == 1:
            drinks = self.controller.return_all_drinks()
            drinks_ids = [drink.id for drink in drinks]
            last_id_drinks = max(drinks_ids) + 1 if drinks_ids else 1
            drink_price = int(input('Enter the price of the drink: '))
            drink_alc_content = int(input('Enter the alcohol content of the drink: '))

            self.controller.add_drink(last_id_drinks, drink_price, drink_alc_content)

        elif choice == 2:
            self.controller.print_drinks()

        else:
            self.manage_menu()

    def manage_orders(self):
        print('''

                       1. Add order
                       2. Show total cost for one order
                       3. Show bill
                       4. Show all orders
                       5. Exit

                       ''')

        choice = int(input('Your choice: '))

        if choice == 1:

            orders = self.controller.return_all_orders()
            orders_ids = [order.id for order in orders]
            last_id_orders = max(orders_ids) + 1 if orders_ids else 1

            cust_id = int(input('Enter the customers ID: '))
            ids_of_dishes = []
            dishes_number = int(input('Enter how many dishes are in the order: '))

            i = 0
            while i < dishes_number:
                id_of_dish = int(input('Enter the ID of the dish: '))
                ids_of_dishes.append(id_of_dish)
                i += 1

            ids_of_drinks = []
            drinks_number = int(input('Enter how many drinks are in the order: '))

            j = 0
            while j < drinks_number:
                id_of_drink = int(input('Enter the id of the drink: '))
                ids_of_drinks.append(id_of_drink)
                j += 1

            self.controller.add_order(last_id_orders, cust_id, ids_of_dishes, ids_of_drinks)

        elif choice == 2:
            id = int(input('Enter the id of the order: '))
            orders = self.controller.OrderRepo.load_to_list()

            for order in orders:
                if order.id == id:
                    self.controller.show_total_cost(order)
                    break

        elif choice == 3:

            '''
            id = int(input('Enter the id of the order: '))
            cust_id = int(input('Enter the customers ID: '))
            ids_of_dishes = []
            dishes_number = int(input('Enter how many dishes are in the order: '))

            i = 0
            while i < dishes_number:
                id_of_dish = int(input('Enter the ID of the dish: '))
                ids_of_dishes.append(id_of_dish)
                i += 1

            ids_of_drinks = []
            drinks_number = int(input('Enter how many drinks are in the order: '))

            j = 0
            while j < drinks_number:
                id_of_drink = int(input('Enter the id of the drink: '))
                ids_of_drinks.append(id_of_drink)
                j += 1

            order = Order(id, cust_id, ids_of_dishes, ids_of_drinks)
            print(order.show_bill(self.controller.cookedDish_repo, self.controller.drink_repo))

            '''

            id = int(input('Enter the id of the order: '))
            orders = self.controller.return_all_orders()

            for order in orders:
                if order.id == id:
                    print(order.show_bill(self.controller.CookedDishRepo, self.controller.DrinkRepo))
                    break

        elif choice == 4:
            self.controller.print_orders()

        else:
            self.main_menu()

    def main_menu(self):
        while True:
            print("""

                        1. Manage Customers
                        2. Manage Menu
                        3. Manage Orders
                        4. Exit


                        """)

            choice = int(input('Your choice: '))

            if choice == 1:
                self.manage_customers()

            elif choice == 2:
                self.manage_menu()

            elif choice == 3:
                self.manage_orders()

            elif choice == 4:
                break

            else:
                print('Invalid choice!!!')