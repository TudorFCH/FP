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