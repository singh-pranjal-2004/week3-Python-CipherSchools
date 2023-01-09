# OBJECTIVES
# WHAT IS CLASS 
# HOW TO CREATE IN CLASS 
# WHAT IS INIT METHOD 
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT 

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print('init method called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Pranjal', 'Singh', 18)
p2 = Person('Harsh', 'Singh', 18)

print(p1.first_name)
print(p2.first_name)