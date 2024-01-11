'''
Test to see if the add cooked Dish functionality works
'''

from modelle.gekochtergericht import GekochterGericht
from repository.CookedDishRepo import CookedDishRepo

d1 = GekochterGericht(1, 100, 15, 350)
d2 = GekochterGericht(2, 200, 20, 350)

repo = CookedDishRepo()

def test_add_to_list():
    repo.add_cookedDishes(d1)
    repo.add_cookedDishes(d2)

    assert len(repo.cookedDishes) != 0

test_add_to_list()

def test_add_to_file():
    repo.add_cookedDishes(d1)
    repo.add_cookedDishes(d2)
    repo.save()

    assert repo.filename

test_add_to_file()