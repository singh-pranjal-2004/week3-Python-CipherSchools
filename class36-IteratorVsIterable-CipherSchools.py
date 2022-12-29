# iterator vs iterables

numbers = [1,2,3,4] # list, tuplels, iterables
squares = map(lambda a: a**2, numbers) # iterator

print(next(numbers))