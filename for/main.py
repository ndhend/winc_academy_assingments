from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """


#=========================================================================================================

# print(countries) check list

# shortest_names: takes a list of item names -> def blabla(mylist):
# returns a list of item names -> new list for item names -> []
#  that have the shortest length -> shortest (value it needs to compare to), lenght-> function len

def shortest_names(mylist):
    name_list = []
    shortest_name = 100
    for name in mylist:
        name_len = len(name)
        if name_len < shortest_name:
            shortest_name = name_len
            name_list = [name]
        elif name_len == shortest_name: # bij if ipv elif krijg ik Chad dubbel
            name_list.append(name)
    return name_list
print(shortest_names(countries))

# most_vowels takes a list -> mylist
# gives a list -> empty list: []
# countries with the most vowels -> vowels: 'abcdefghijklmnopqrstuvwxyz'
# vowel_count = 0, vowel_count=+1
# gives 3 countries with the most vowels from most to least ->
# index [:3]; sort Reverse=True

def most_vowels(my_list):
        vowels = "aeiou"
        most_vowels_list = [] # lege lijst daar de output een lijst moet zijn.
        num_name_list = []
        for name in my_list: # zit pas in de loop na identation
            vowels_count = 0 # we willen de landen met de meeste klinkers
            for letter in name.lower():
                if letter in vowels: # it.countrystring vgl met it.vowelstr als True + 1
                    vowels_count += 1
            num_name_list.append([vowels_count, name])
            num_name_sorted = sorted(num_name_list, reverse=True)[:3] # sorteert altijd op de eerste variable
        for num_name in num_name_sorted:
             most_vowels_list.append(num_name[1])
        return most_vowels_list
print(most_vowels(countries))

def alphabet_set(my_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet)
    for name in  my_list:
        for char in name:
            if char in alphabet_list: 
               alphabet_list.remove(char) # elke keer een letter halen uit de lijst
               if name not in alphabet_list:
                  alphabet_list.append(name)
    return alphabet_list
print(alphabet_set(countries))