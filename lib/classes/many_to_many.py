class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise ValueError(
                'Name cannot be re-assigned.'
            )
        elif isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise TypeError(
                'Name must be a string between 1 and 15 characters.'
            )
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum(order.price for order in self.orders()) / self.num_orders()

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and len(name) < 16:
            self._name = name
        else: 
            raise TypeError(
                'Name must be a string between 1 and 15 characters.'
            )

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Dictionary for storing customers and total they have spent on one kind of coffee in k:v pairs.
        cust_and_sum = {}

        for customer in cls.all:
            # Iterate once through all customers
            cust_sum = sum([order.price for order in customer.orders() if order.coffee == coffee])
            # If the customer has any order history with that coffee...
            if cust_sum:
                # ... add their name and total they've spent on that coffee to {cust_and_sum}.
                cust_and_sum[customer.name] = cust_sum
        
        # If that coffee has been ordered...
        if cust_and_sum:
            # Establish the highest amount paid for that coffee by one person.
            top_sum = max(cust_and_sum.values())
            # Retrieve the customer(s) from {cust_and_sum} whose sum matches the top sum.
            top_list = [customer for customer, sum in cust_and_sum.items() if sum == top_sum ]
            # Return a single customer or a list of customers if there is a tie.
            return top_list[0] if len(top_list) == 1 else top_list
        # If there is no order history for that coffee, return None.
        else:
            return None
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            raise ValueError(
                'Price cannot be re-assigned.'
            )
        elif isinstance(price, float) and price >= 1.0 and price <= 10.0:
            self._price = price
        else:
            raise TypeError(
                'Price must be a float between 1.0 and 10.0.'
            )
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise TypeError(
                'Customer must be of the Customer class.'
            )
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise TypeError(
                'Coffee must be of the Coffee class.'
            )
