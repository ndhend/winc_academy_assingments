# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

''''# Write a function alphabetical_order that takes one argument: a list of strings that represent film names
# Function: def alphabetical_order; argument () film_names
# It returns a list of the same films in alphabetical order. 
# sorting lists

# list of strings that represent film names. 

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

# Write a function alphabetical_order that takes one argument: a list of strings that represent film names
# It returns a list of the same films in alphabetical order. 
# sorting lists: 2 ways
# 1. sorted_list = sorted(mylist) print(sorted_list)
# 2. mylist.sort() print(mylist)

def alphabetical_order (my_list):
    alphabetical_order = sorted(my_list)
    return alphabetical_order
#print(alphabetical_order(film_names))

# Write a function won_golden_globe that takes a film name 
# and returns True or False based on whether or not this movie won a Golden Globe.

# golden globe list with movies that won golden globe

golden_globe_list = [
    'Jaws',
    'Star Wars',
    'E.T',
    'Memoirs of a Geisha'
]

#  Look into using the lower-function on the given film string
# my_list = [s.lower() for s in my_list]
film_names = [s.lower() for s in film_names]
golden_globe_list = [s.lower() for s in golden_globe_list]

def won_golden_globe(movie_name):
    if movie_name.lower() in golden_globe_list:
        return True
    return False
 
print(won_golden_globe('The River'))

# lower function as function for an argument is
# argument = argument.lower()"""

# John's son Joseph accidentally mixed in some of his own work as lead singer for Toto
#  with a list of his dad's compositions. 
# Write a function remove_toto_albums that takes a list of strings, 
# removes Joseph's Toto albums from it and returns the tidy list.

# mixed_list 



# Write a function remove_toto_albums that takes a list of strings, 
# removes Joseph's Toto albums from it and returns the tidy list.

# function: removes Joseph's Toto Albums from list and returns tidy list
# outcome = tidy list
# argument is mixed list

"""my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
strings_to_remove = ['banana', 'date']

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
strings_to_remove = ['banana', 'date']

#new_list = [item for item in my_list if item not in strings_to_remove]

#print(new_list)"""

def remove_toto_albums(my_list):
    remove_toto_albums= [item for item in my_list if item not in toto_list]
    return remove_toto_albums
#print(remove_toto_albums(mixed_list))

"""new_list = list(filter(lambda x: x not in strings_to_remove, my_list))

print(new_list)

def remove_toto_albums(my_list):
    remove_toto_albums = list(filter(lambda x: x not in toto_list, my_list))
    return remove_toto_albums
print(remove_toto_albums(mixed_list))'''

# Write a function alphabetical_order that takes one argument: 
# a list of strings that represent film names
#  returns a list of the same films in alphabetical order
#  sorting lists: list_name.sort
# make list of strings film_names

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
def remove_toto_albums(mixed_with_toto_albums):
    if str() in mixed_with_toto_albums:
        mixed_with_toto_albums.remove(str())
        return mixed_with_toto_albums
    
print (remove_toto_albums("Toto XVI"))
print (remove_toto_albums(mixed_with_toto_albums))