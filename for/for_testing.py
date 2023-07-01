#shortest_names: takes a list of country names 
# and returns a list of country names that have the shortest length.

# see Edx -> set a starting point 
# shortest lenght -> len function (len)

test_name_list = [ 'chad', 'argentina', 'jerusalem', 'iran', 'iraq', 'test']

'''def shortest_names(my_list):
    shortest_len = 100
    shortest_len_name = []
    for item in my_list:
        #item_len = len(item)
        if len(item) < shortest_len:
            shortest_len = len(item)
            shortest_names = [item]
        elif len(item) == shortest_len:
            shortest_names.append(item)
    return shortest_names
    
print(shortest_names(test_name_list))'''

# most_vowels: takes a list of country names
# and returns a list with the top three countries that have the most vowels in their name.
# 1. lijst maken met vowels
# 2. lijst in volgorde plaatsen van lengte
# def most_vowels(countries):
#  vowel_list = []
#  for country in countries:
#      vowel_count = 0
#      for letter in countries:
# bedenk welke stappen je nodig hebt (wat)
# bedenk hoe je die stappen gaat maken (googlen) hoe

# functie waarbij ik vowels uit een string haal uit een lijst
# en een nieuwe lijst maak met de vowelstrings.
# hoe haal ik vowels uit een string?

'''for char in 'abcdefg': # behandelt string als een lijst itereert over elk item in de lijst
    if char in 'ae': # behadelt string als een lijst itereert over elk item in de lijst
        print(char)
    else:
        print(False)
# See output

a (a)
False (b)
False (c)
False (d)
e (e)
False (f)
False (g)


def vowels(string):
    vowels = '' # lege string
    for char in string: # voor elke letter in de string
        if char.lower() in "aeiou":
            vowels += char # wordt de letter bij de string opgeteld, alsof het een lijst is

  #print(vowels('Chaeiod'))

# functie waarbij ik uit alle strings in de lijst de klinkers haal
# vorig functie in functie en lege lijst maken met de klinkerstrings

def vowels_list(my_list):
    vowels_list = [] # lege lijst met vowelstrings
    for string in my_list:
        def vowels(string):
            vowels = ''
            for char in string:
                if char.lower() in "aeiou":
                    vowels += char
            return vowels
        vowels_list.append(vowels(string))
    return vowels_list'''

 # foutieve versie
test_list = [ 'chad', 'argentina', 'jerusalem', 'iran', 'iraq', 'test']
'''def num_name(my_list):
    num_name_list = []
    for name in my_list:
        vowels_count = 0
        for char in name.lower():
            if char in "aeiou":
                vowels_count += 1
        num_name_list.append([name, vowels_count]) # diff identation, diff results'''

'''def vowels_list(my_list):
    vowels_list = [] # lege lijst, daar de output een lijst moet zijn landen
    for string in my_list:
        def vowels(string): # eerst een functie maken die de klinkers neemt uit de landen 
            vowels_count = 0 # vergelijkt it string met it vowelstring en telt 1 op bij True
            for char in string:
                if char.lower() in "aeiou":
                    char = len(char)
                    # vowels_count = 0 output = [1, 1, 1, 1, 1, 1]???
                    vowels_count += 1
            return vowels_count # Traceback als ik deze eruit haal, waarom?
        vowels_list.append(vowels(string))
        vowels_list.sort(reverse=True)
    return vowels_list
print(vowels_list(test_list))'''
        
        

     
        
        
        #sorted(num_name_list, key=lambda x: x[1], reverse=True)[:3]
        
            
#key = lambda to specify the sorting key
# why I don't get 4 countries with [:3] and just 2 with [:2]
# I expected, as it is a list 0,1,2(,3)
   


print(most_vowels(test_list))                      


# nu we een lijst hebben met 2 waarden willen we de lijst sorteren op landen met de meeste klinkers
# daarvan willen vervolgens de eerste 3 landen
# lijst sorteren op vowel_count [0:1] dus sorteren op 1.
# vervolgens willen we niet de vowel_count maar de naam van de landen in een lijst
# in die lijst willen we alleen de eerste 3 landen in de nieuwe lijst met landen.

# print(dir(num_name(test_list))) met dir() kan je zien welke functies je kan toepassen bij een object
# sorted_list = sorted(num_name(test_list))
#print(sorted_list)
# print(object(tuple))


     
     

    


#print(num_name(test_list))
    


    


# num_name.append under if-> output
'''
[['chad', 0], ['chad', 0], ['chad', 1], ['chad', 1], ['argentina', 1],
 ['argentina', 1], ['argentina', 1], ['argentina', 2], ['argentina', 2], 
 ['argentina', 2], ['argentina', 3], ['argentina', 3], ['argentina', 4], 
 ['jerusalem', 0], ['jerusalem', 1], ['jerusalem', 1], ['jerusalem', 2], 
 ['jerusalem', 2], ['jerusalem', 3], ['jerusalem', 3], ['jerusalem', 4], 
 ['jerusalem', 4], ['iran', 1], ['iran', 1], ['iran', 2], ['iran', 2], 
['iraq', 1], ['iraq', 1], ['iraq', 2], ['iraq', 2], ['test', 0], ['test', 1], 
['test', 1], ['test', 1]]
'''



'''test_list = [ 'chad', 'argentina', 'jerusalem', 'iran', 'iraq', 'test']
def num_name(my_list):
    num_name = []
    for name in my_list:
        vowels_count = 0
        for char in name.lower():
            if char in "aeiou":
                vowels_count += 1
        num_name.append([name, vowels_count])
    return num_name
print(num_name(test_list))'''

'''def shortest_name(my_list):
    shortest_len = 1000 # een waarde bepalen waarmee de lengte vergeleken wordt
    shortest_len_name = [] # een lege lijst waarin de landen komen te staan met de korste lengte
    for item in my_list:
        item_len = len(item) 
        if item_len < shortest_len:
            # Updating the value of 'shortest_len' with the current shortest length
            shortest_len = item_len
            # Creating a new list with the current item as the only item
            shortest_names = [item]
        # Checking if the current item name has the same length as the current shortest length
        elif item_len == shortest_len:
            # Adding the current item to the list of shortest item names
            shortest_names.append(item)
            # Returning the list of shortest item names
    return shortest_names
print(shortest_name(countries))

def shortest_names(my_list):
    shortest_len = 100
    shortest_len_name = []
    for item in my_list:
        item_len = len(item)
        if len(item) < shortest_len:
            shortest_len = item_len
            shortest_names = [item]
        elif item_len == shortest_len:
           shortest_names.append(item)
    return shortest_names
    
print(shortest_names(countries))'''

# most_vowels: takes a list of country names
# and returns a list with the top three countries that have the most vowels in their name.
# 1. lijst maken met vowels
# 2. lijst in volgorde plaatsen van lengte
# def most_vowels(countries):
#  vowel_list = []
#  for country in countries:
#      vowel_count = 0
#      for letter in countries:
# bedenk welke stappen je nodig hebt (wat)
# bedenk hoe je die stappen gaat maken (googlen) hoe

# functie waarbij ik vowels uit een string haal uit een lijst
# en een nieuwe lijst maak met de vowelstrings.
# hoe haal ik vowels uit een string?

def vowels(string):
    vowels = '' # lege string
    for char in string:
        if char.lower() in "aeiou":
            vowels += char
    return vowels
#print(vowels('Chaeiod'))

# functie waarbij ik uit alle strings in de lijst de klinkers haal
# vorig functie in functie en lege lijst maken met de klinkerstrings

'''def vowels_list(my_list):
    vowels_list = []
    for string in my_list:
        def vowels(string):
            vowels = ''
            for char in string:
                if char.lower() in "aeiou":
                    vowels += char
            return vowels
        vowels_list.append(vowels(string))
    return vowels_list

# print(vowels_list(countries))

# een functie die de lengte van de vowelsstrings teruggeeft
# eerst een functie die de lengte van 1 string teruggeeft.

'''
# countries = ('Aruba', 'Chad', 'China', 'Korea', 'Japan')
def vowels(string):
    vowels = 0
    for char in string:
        if char.lower() in "aeiou":
            char = len(char)
            vowels += 1
    return vowels
# print(vowels('Chad'))'''

# functie vowels_list aanpassen met nieuwe functie


# functie aanpassen zodat ik de lengte van de klinkers op volgorde krijg.

'''def vowels_list(my_list):
    vowels_list = []
    vowels_count = 0
    for string in my_list:
        def vowels(string):
            vowels = 0
            for char in string:
                if char.lower() in "aeiou":
                    char = len(char)
                    vowels += 1
            return vowels
        vowels_list.append(vowels(string))
        vowels_list.sort(reverse=True)
    return vowels_list
print(vowels_list(countries))'''
    
# functie aanpassen zodat ik de namen terugkrijg met de langste klinkerstrings
# eerst een functie met zowel klinkerlengte als naam van het land in een lijst
# daarvoor functie waarbij ik een string in een lijst krijg

# I want a new list with name of the country and the vowel length
'''def num_name(my_list):
    num_name = []
    for name in my_list:
        vowels_count = 0
        for char in name.lower():
            if char in "aeiou":
                vowels_count += 1
        num_name.append([name, vowels_count])
    return num_name
print(num_name(countries))
num_name_list = num_name(countries)
# print(num_name_list)

# maak een functie waarbij je de num_name_list sorteert op vowel length descending
# descending reverse=True
# van ChatGPT
def sort_by_second_element(my_list):
    return my_list[1] # geeft de plek aan in de lists in de list [0;1]
num_name_list.sort(key=sort_by_second_element, reverse=True)
(num_name_list)

# een functie die alleen de landen weergeeft in volgorde van meeste klinkers
def most_vowels(my_list):
    names_list = []
    for item in num_name_list:
        name = item[0]  # extract the name from the sublist
        names_list.append(name)  # add the name to the new list
    return names_list[:3]
print(most_vowels(countries))
# print(type(names_list))

# most_vowels = names_list[:3]
# print(most_vowels)

# alphabet_set: takes a list of country names and returns a list of country names whose
# letters can be combined to form the complete alphabet.'''

'''def most_vowels(my_list):
        most_vowels_list = [] # lege lijst daar de output een lijst moet zijn.
        for name in my_list:
            vowels_count = 0 # we willen de landen met de meeste klinkers
            for letter in name.lower():
                if letter in "aeiou": # it.countrystring vgl met it.vowelstr als True + 1
                    vowels_count += 1
            most_vowels_list.append([name,vowels_count])
        return sorted(most_vowels_list, key=lambda x: x[1], reverse=True)[:3]
print(most_vowels(countries))'''

# onderstaande formule werkt maar geeft mij 46 landen, het mogen er mx 14 zijn      
def unique_country_char_list(my_list):
        country_list = set()
        unique_chars = set()
        for string in my_list:
            for char in string:
                unique_chars.add(char.upper())
                country_list.add(string)
            if len(unique_chars) == 26:
                return unique_chars # country_list veranderd in unique_chars
   
   
print(unique_country_char_list(countries))

'''def alphabet_set(country_list):
    alphabet = "abcdefghijklmnopqrstuwvxyz"
    checked_countries = []
    found_letters = []
    for country in country_list:
        ContainsNewLetter = False
        for c in country:
            character = c.lower()
            if character in alphabet:
                if character not in found_letters:
                    ContainsNewLetter = True
                    found_letters.append(character)
        if ContainsNewLetter:
            checked_countries.append(country)
        if len(checked_countries) <= 14 and len(found_letters) == 26:
            return checked_countries
#print(alphabet_set(countries))'''










 
           




def bla(x):
    celsius = (x-32)*5/9
    return celsius
print(bla(1))
