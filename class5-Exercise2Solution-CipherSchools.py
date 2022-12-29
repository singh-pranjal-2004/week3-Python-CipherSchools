# users = {
#     'name' : 'Pranjal',
#     'age' : '19',
#     'fav_movies' : ['avengers', 'lucifer'],
#     'fav_songs' : ['mann mera', 'tu hi haqeeqat']
# }
user = {}

name = input('What is your name : ')
age = input('what is you age : ')
fav_movies = input('what are you fav movies separated by comma ').split(',')
fav_songs = input('what are you fav songs separated by comma ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

for key,value in user.items():
    print(f"{key} : {value}")