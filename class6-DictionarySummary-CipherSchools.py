# summary dictionary
# what is dictionary
# unordered collection of data

d = {'name' : 'Pranjal', 'age' : 18}

# or
d1 = dict(name = 'Pranjal', age = 24)

# or 

d2 = {
    'name' : 'Pranjal',
    'age' : '18',
    'fav_movies' : []
}


# how to access data from dictionary
# you cannot do like
# d[0] , because there is no order inside dictionary

# syntax
# print(dictname[keyname])
print(d['name'])


# add data inside empty dict 
empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
print(empty_dict)

# check existence of values inside dict 
# use in keyword to check for keys 



# how to iterate over dictionary
# most commonly method
# for key, value in d.items():
#     print(f'key is {key} and value is {value} ')

# to print all keys

# for i in d:
#     print(i)

# to print all values 
# for i in d.values():
#     print(i) 


# most common dict mehtods

# get method 
# to access a key and check existence
# print(d.get('name'))

# Q - why we use get 
# A - to get rid of error
# example
# print(d['name'])
# print(d.get('name'))


# to delete item 
# pop ---> take one argument which is keyname 

# popped = d.pop('name')
# print(popped)
# print(d)

# pop item 
popped = d.popitem()
print(popped)
print(d)