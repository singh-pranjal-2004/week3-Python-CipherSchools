# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} : {v}')

# dictionary unpacking
d = {'name':'Pranjal', 'age' : 18}
# func(first_name = 'Pranjal', last_name = 'Singh')
func(**d)