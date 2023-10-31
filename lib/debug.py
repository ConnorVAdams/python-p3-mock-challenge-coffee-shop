#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

coffee = Coffee("Mocha")
coffee_2 = Coffee("Frapp")
coffee_3 = Coffee("Drip")
customer = Customer('Wayne')
customer_2 = Customer('Dima')
customer_3 = Customer('Dennis')
order_1 = Order(customer, coffee_2, 10.0)
order_2 = Order(customer_2, coffee, 5.0)
order_3 = Order(customer_3, coffee, 2.0)
order_4 = Order(customer_3, coffee_2, 5.0)
order_5 = Order(customer, coffee, 2.0)
order_6 = Order(customer_3, coffee_2, 5.0)

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    ipdb.set_trace()
