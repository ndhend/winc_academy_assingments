# list of strings 
film_names = [ 
    'Tom Sawyer',
    'Earthquake',
    'Jaws',
    'Star Wars',
    'Superman',
    'E.T',
    'The River',
    'Schindler\'s List',
    'Memoirs of a Geisha',
    'War Horse',
    'Lincoln'
]

# function alphabetical_order
# .sort() or sorted()
def alphabetical_order(my_list):
    alphabetical_order = sorted(my_list)
    return alphabetical_order
print(alphabetical_order(film_names))

#Write a function won_golden_globe that takes a film name 
# and returns True or False based on whether or not this movie won a Golden Globe.

# make list of movies that won golden globe
golden_globe_list = [
    'jaws',
    'star wars',
    'e.t',
    'memoirs of a geisha'
]

'''golden_globe_lower = []
for globe_movie in golden_globe_list:
    golden_globe_lower.append(globe_movie.lower())'''


# function that returns True when in list Golden Globe 
#  otherwise False.

def won_golden_globe(movie_name):
    if movie_name.lower() in golden_globe_list:
        return True
    else:
        return False
print(won_golden_globe('E.T'))

# make mixed_list 
# make toto_list
mixed_list = [
    'Tom Sawyer',
    'Earthquake',
    'Miss Sun',
    'Jaws',
    'Fahrenheit',
    'Star Wars',
    'Superman',
    'E.T',
    'The River',
    'Lea',
    'Last Night',
    'Old Is New'
]

toto_list = [ 
    'Miss Sun',
    'Fahrenheit',
    'Lea',
    'Last Night',
    'Old Is New'
    ]

# function Write a function remove_toto_albums 
# that takes a list of strings, 
# removes Joseph's Toto albums from it and returns the tidy list.

def remove_toto_albums(my_list):
    if "Fahrenheit" in my_list:
        my_list.remove("Fahrenheit")
    if 'Lea' in my_list:
        my_list.remove('Lea')
    if 'Old Is New' in my_list:
        my_list.remove('Old Is New')
    return my_list
def remove_toto_albums(my_list):
    for item in my_list:
        if item in toto_list: 
            my_list.remove(item)
            return remove_toto_albums

print(remove_toto_albums(mixed_list))



