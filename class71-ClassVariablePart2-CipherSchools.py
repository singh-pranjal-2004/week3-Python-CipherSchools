# change class variable
# how to print name space for objects
# What if we use self instead of class name for class variables
# 

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        # instance variables
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self):
        # self.price
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price



laptop1 = Laptop("Mi", 'Notebook 15 Pro', 40000)
laptop2 = Laptop("Apple", 'MacBook pro', 230000)
print(laptop2.__dict__)
laptop2.discount_percent = 50
print(laptop2.apply_discount())