# base class
class smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"
    def get_price(self):
        return self.price
    def set_price(self, new_price):
        self.price = new_price          

#derived class
class smartphone_5g(smartphone):
    def __init__(self, brand, model, price, network_type):
        super().__init__(brand, model, price)
        self.network_type = network_type

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Network Type: {self.network_type}"
    def get_network_type(self):
        return self.network_type
    def set_network_type(self, new_network_type):
        self.network_type = new_network_type
    def get_price(self):
        return self.price
    def set_price(self, new_price):
        self.price = new_price
    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Network Type: {self.network_type}"
    def get_network_type(self):
        return self.network_type
    def set_network_type(self, new_network_type):
        self.network_type = new_network_type
    def get_price(self):
        return self.price
    def set_price(self, new_price):
        self.price = new_price
    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Network Type: {self.network_type}"
#polymorphism
class smartphone_4g(smartphone):
    def __init__(self, brand, model, price, network_type):
        super().__init__(brand, model, price)
        self.network_type = network_type

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Network Type: {self.network_type}"
    def get_network_type(self):
        return self.network_type
    def set_network_type(self, new_network_type):
        self.network_type = new_network_type
    def get_price(self):
        return self.price
    def set_price(self, new_price):
        self.price = new_price
#another derived class
class smartphone_3g(smartphone):
    def __init__(self, brand, model, price, network_type):
        super().__init__(brand, model, price)
        self.network_type = network_type

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Network Type: {self.network_type}"
    def get_network_type(self):
        return self.network_type
    def set_network_type(self, new_network_type):
        self.network_type = new_network_type
    def get_price(self):
        return self.price
    def set_price(self, new_price):
        self.price = new_price
# Testing the classes
my_smartphone_5g = smartphone_5g("Samsung", "Galaxy S21", 799, "5G")
my_smartphone_4g = smartphone_4g("Apple", "iPhone 12", 699, "4G")
my_smartphone_3g = smartphone_3g("Nokia", "3310", 49, "3G")
print(my_smartphone_5g.get_details())
print(my_smartphone_4g.get_details())
print(my_smartphone_3g.get_details())
# Output:
# Brand: Samsung, Model: Galaxy S21, Price: 799, Network Type: 5G
