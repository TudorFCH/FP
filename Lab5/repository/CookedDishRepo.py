import pickle
from repository.DataRepo import DataRepo

class CookedDishRepo(DataRepo):

    def __init__(self):

        super().__init__("CookedDishRepo.txt")
        self.cookedDishes = []

    def add_cookedDishes(self, cooked_dish):
        self.cookedDishes.append(cooked_dish)

    def save(self):
        with open(self.filename, 'wb') as f:
            for cooked_Dish in self.cookedDishes:
                pickle.dump(cooked_Dish, f)
                f.write(b'\n')


    def load(self):
        self.cookedDishes = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()
                try:
                    cookedDish = pickle.load(f)
                    self.cookedDishes.append(cookedDish)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    f.seek(position)
                    f.readline()

    def get_cookedDishID(self, dish_id):
        for dish in self.cookedDishes:
            if dish.id == dish_id:
                return dish
        return None

    def load_to_list(self):
        self.cookedDishes = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()
                try:
                    cookedDish = pickle.load(f)
                    self.cookedDishes.append(cookedDish)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    f.seek(position)
                    f.readline()

        return self.cookedDishes


    def read_file(self):
        file_content = []
        f = open(self.filename, 'rb')

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


    def convert_to_string(self):
        pass

    def convert_from_string(self, filename, str_list):
        pass