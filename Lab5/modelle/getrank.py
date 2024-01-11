from modelle.gericht import Dish

class Getrank(Dish):
    def __init__(self, id, price, alc_content):
        super().__init__(price, id)
        self.alc_content = alc_content
        self.drinks = []

    def __repr__(self):
        return f'Drink: ID = {self.id}, Price = {self.price}, Alcohol Content = {self.alc_content}'