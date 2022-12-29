# zip function 
user_id = ['user1', 'user2', 'user3']
names = ['pranjal', 'harsh', 'betu']
last_names = ['singh', 'kumar', 'sharma']

# ('user1', 'pranjal'), ('user2', 'harsh')
print(dict(zip(user_id, names, last_names)))

# example = [('a',1), ('b',2)]
# print(dict(example))