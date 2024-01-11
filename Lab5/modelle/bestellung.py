from modelle.identifiable import Identifiable
from functools import reduce
from repository.CookedDishRepo import CookedDishRepo
from repository.DrinkRepo import DrinkRepo


class Bestellung(Identifiable):
    def __init__(self, id, customer_id, list_of_dish_id: list, list_of_drink_id: list):
        super().__init__(id)
        self.customer_id = customer_id
        self.list_of_dish_id = list_of_dish_id
        self.list_of_drink_id = list_of_drink_id

    def __repr__(self):
        return (f'Order: ID = {self.id}, Customer ID = {self.customer_id}, '
                f'IDs of Dishes = {self.list_of_dish_id}, '
                f'IDs of Drinks = {self.list_of_drink_id}')

    def calc_cost(self, dish_repo: CookedDishRepo, drink_repo: DrinkRepo):
        def calculate_total_cost(total, item):
            dish = dish_repo.get_cookedDishID(item)
            if dish:
                return total + dish.price
            return total

        total_dish_cost = reduce(calculate_total_cost, self.list_of_dish_id, 0)

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




