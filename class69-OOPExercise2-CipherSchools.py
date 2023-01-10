class Laptop:
    def __init__(self, brand, model_name, price):
        # instance variables
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self,num):
        # self.price
        off_price = (num/100)*self.price
        return self.price - off_price


laptop1 = Laptop("Mi", 'Notebook 15 Pro', 40000)
laptop2 = Laptop("Apple", 'MacBook pro', 230000)
print(laptop2.apply_discount(10))