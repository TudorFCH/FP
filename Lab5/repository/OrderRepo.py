import pickle
from functools import reduce

from repository.DrinkRepo import DrinkRepo
from repository.CookedDishRepo import CookedDishRepo
from repository.DataRepo import DataRepo

class OrderRepo(DataRepo):

    def __init__(self):

        super().__init__("OrderRepo.txt")
        self.filename = self.__class__.__name__ + ".txt"
        self.orders = []

    def add_orders(self, order):
        self.orders.append(order)

    def save(self):
        with open(self.filename, 'wb') as f:
            for order in self.orders:
                pickle.dump(order, f)
                f.write(b'\n')

    def load(self):
        orders = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()
                try:
                    order = pickle.load(f)
                    self.orders.append(order)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    f.seek(position)
                    f.readline()



    def load_to_list(self):
        self.orders = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()
                try:
                    order = pickle.load(f)
                    self.orders.append(order)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    f.seek(position)
                    f.readline()

        return self.orders



    def read_file(self):
        f = open(self.filename, 'rb')
        file_content = []

        while True:

            try:
                current_obj = pickle.load(f)
                file_content.append(current_obj)
            except EOFError:
                break

        f.close()
        return file_content


    def write_to_file(self, string):
        f = open(self.filename, 'ab')
        pickle.dump(string, f)
        f.close()

    def calc_cost(self, dish_repo: CookedDishRepo, drink_repo: DrinkRepo):
        def calculate_total_cost_food(total, item):
            dish = dish_repo.get_cookedDishID(item)
            if dish:
                return total + dish.price
            return total

        total_dish_cost = reduce(calculate_total_cost_food, self.list_of_dish_id, 0)

        def calculate_total_cost_drink(total, item):
            drink = drink_repo.get_drink_id(item)
            if drink:
                return total + drink.price
            return total

        total_drink_cost = reduce(calculate_total_cost_drink, self.list_of_drink_id, 0)

        total_cost = total_dish_cost + total_drink_cost

        return (
            f'Total Dish Cost = {total_dish_cost} \nTotal Drink Cost = {total_drink_cost} \nTotal Order Cost = {total_cost}')

    def bill(self, dish_repo: CookedDishRepo, drink_repo: DrinkRepo):
        dishes = {}
        drinks = {}

        for dish_id in self.list_of_dish_id:
            dish = dish_repo.get_cookedDishID(dish_id)
            if dish:
                dishes[dish.id] = dish.price

        for drink_id in self.list_of_drink_id:
            drink = drink_repo.get_drink_id(drink_id)
            if drink:
                drinks[drink.id] = drink.price

        return dishes, drinks

    def show_bill(self, dish_repo, drink_repo):
        result1, result2 = self.bill(dish_repo, drink_repo)
        return f'The List of Orderd Dishes: {result1} \n The List of Orderd Drinks: {result2}'


    def convert_to_string(self):
        pass

    def convert_from_string(self, filename, string):
        pass

