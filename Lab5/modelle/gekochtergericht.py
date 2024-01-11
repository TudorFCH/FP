from modelle.gericht import Dish

class GekochterGericht(Dish):
    def __init__(self, id, price, preparation_time, portion_size = 350):
        super().__init__(price, id, portion_size)
        self.preparation_time = preparation_time

    def __repr__(self):
        return f'Cooked Dish: ID = {self.id}, Price = {self.price}, Preparation Time = {self.preparation_time}, Portion Size = {self.portion_size}'

