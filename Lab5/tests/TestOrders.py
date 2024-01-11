'''
Test the functionality for orders
'''

from modelle.bestellung import Bestellung
from repository.OrderRepo import OrderRepo
from modelle.kunde import Kunde
from repository.CustomerRepo import CustomerRepo
from modelle.getrank import Getrank
from repository.DrinkRepo import DrinkRepo
from modelle.gekochtergericht import GekochterGericht
from repository.CookedDishRepo import CookedDishRepo

o1 = Bestellung(1, 1, [1, 2], [1, 2])
o2 = Bestellung(2, 1, [1], [2])

c1 = Kunde(1, 'Alexandru', 'Bihorului')
c2 = Kunde(2, 'Tudor', 'Nicolae Iorga')

dr1 = Getrank(1, 30, 15)
dr2 = Getrank(2, 50, 30)

d1 = GekochterGericht(1, 100, 15)
d2 = GekochterGericht(2, 200, 30)

repo_orders = OrderRepo()
repo_dishes = CookedDishRepo()
repo_drinks = DrinkRepo()
repo_customers = CustomerRepo()

repo_dishes.add_cookedDishes(d1)
repo_dishes.add_cookedDishes(d2)
repo_dishes.save()

repo_drinks.add_drinks(dr1)
repo_drinks.add_drinks(dr2)
repo_drinks.save()

repo_customers.add_customers(c1)
repo_customers.add_customers(c2)
repo_customers.save()

repo_orders.add_orders(o1)
repo_orders.add_orders(o2)
repo_orders.save()

def test_bill():

    dishes = o1.bill(repo_dishes, repo_drinks)[0]
    drinks = o2.bill(repo_dishes, repo_drinks)[1]

    assert len(dishes) != 0 and len(drinks) != 0

#test_bill()

def test_save_order_to_file():

    repo_orders.add_orders(o1)
    repo_orders.add_orders(o2)
    repo_orders.save()

    assert repo_orders.filename

test_save_order_to_file()

def test_order_from_file():

    repo_orders.add_orders(o1)
    repo_orders.add_orders(o2)
    repo_orders.save()


    orders = repo_orders.load_to_list()

    assert len(orders) != 0

test_order_from_file()

