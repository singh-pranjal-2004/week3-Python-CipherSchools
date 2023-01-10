class Laptop:
    def __init__(self, brand, model_name, price):
        # instance variables
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name






laptop1 = Laptop("Mi", 'Notebook 15 Pro', 40000)
laptop1.apply_discount(40)