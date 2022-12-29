# advance min() and max()

# numbers = [1,2,4,5,7]
# print(min(numbets))


names = ["Pranjal", "Harsh Singh", "ph"]
print(max(names, key = lambda item : len(item)))

students = {
    'pranjal' : {'score' : 90 , 'age' : 18},
    'harsh' : {'score' : 80, 'age' : 19},
    'betu' : {'score' : 70, 'age' : 20}
}

print(max(students, key = lambda item : students[item]['age']))

# students2 = [
#     {'name' : 'pranjal', 'score' : 90 , 'age' : 18},
#     {'name' : 'harsh' , 'score' : 80, 'age' : 19},
#     {'name' : 'betu' , 'score' : 70, 'age' : 20}
# ]
# print(max(students2, key = lambda item:item.get('age'))['name'])