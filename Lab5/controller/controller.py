from modelle.getrank import Getrank
from modelle.gekochtergericht import GekochterGericht
from modelle.kunde import Kunde
from modelle.bestellung import Bestellung
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo
from repository.CookedDishRepo import CookedDishRepo


class Controller:
    def __init__(self):
        self.DrinkRepo = DrinkRepo()
        self.CustomerRepo = CustomerRepo()
        self.OrderRepo = OrderRepo()
        self.CookedDishRepo = CookedDishRepo()


    def add_customer(self, customer_id, customer_name, customer_address):
        customer = Kunde(customer_id, customer_name, customer_address)
        self.CustomerRepo.add_customers(customer)
        self.CustomerRepo.save()

    def add_drink(self, id, price, alc_content):
        drink = Getrank(id, price, alc_content)
        self.DrinkRepo.add_drinks(drink)
        self.DrinkRepo.save()

    def add_cooked_dish(self, id, price, prep_time, portion_size):
        dish = GekochterGericht(id, price, prep_time, portion_size)
        self.CookedDishRepo.add_cookedDishes(dish)
        self.CookedDishRepo.save()

    def add_order(self, id, customer_id, list_of_dish_id, list_of_drink_id):
        order = Bestellung(id, customer_id, list_of_dish_id, list_of_drink_id)
        self.OrderRepo.add_orders(order)
        self.OrderRepo.save()

    def show_total_cost(self, order: Bestellung):
        print(order.calc_cost(self.CookedDishRepo, self.DrinkRepo))

    def search_for_customer(self, cust_partial_name):
        return self.CustomerRepo.search_after_partial_name_filt2(cust_partial_name)

    def search_for_customer_after_part_address(self, cust_partial_address):
        return self.CustomerRepo.search_after_partial_address_with_filter(cust_partial_address)

    def update_customers_name(self, old_name: str, new_name: str):
        self.CustomerRepo.update_cust_name(old_name, new_name)

    def print_customers(self):
        print(self.CustomerRepo.load_to_list())

    def return_all_customers(self):
        return self.CustomerRepo.load_to_list()

    def return_all_drinks(self):
        return self.DrinkRepo.load_to_list()

    def return_all_cooked_dishes(self):
        return self.CookedDishRepo.load_to_list()

    def return_all_orders(self):
        return self.OrderRepo.load_to_list()

    def print_drinks(self):
        print(self.DrinkRepo.load_to_list())

    def print_cooked_dishes(self):
        print(self.CookedDishRepo.load_to_list())

    def print_orders(self):
        print(self.OrderRepo.load_to_list())