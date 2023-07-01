import random

def choose_random_string(strings):
    if not strings:
        return None  # Return None if the list is empty
    return random.choice(strings)

my_strings = ["Apple", "Banana", "Cherry", "Aardbei", "Elderberry"]
random_string = choose_random_string(my_strings)
#print(random_string)

#I want a list with fruits with the letter 'a' in it.

'''def a_fruit_list():
    num_it = 0
    a_list = []
    fruit = random_string
    while num_it < 10:
        if 'a' in fruit.lower():
            if fruit not in a_list:
                a_list.append(fruit)
                print(fruit)
    num_it += 1
    return a_list
print (a_fruit_list())

import random

def choose_random_string(strings):
    if not strings:
        return None  # Return None if the list is empty
    return random.choice(strings)

my_strings = ["Apple", "Banana", "Cherry", "Aardbei", "Elderberry"]
random_string = choose_random_string(my_strings)
# print(random_string)

# I want a list of fruits with the letter 'a' in it and the total number of fruits with the letter 'a' in it as outcome
def a_fruit_list():
    num_it = 0
    a_list = []
    count = 0
    while num_it < 10:
        fruit = choose_random_string(my_strings)
        if 'a' in fruit.lower():
            if fruit not in a_list:
                a_list.append(fruit)
            num_it += 1
            num_of_fruit = len(a_list)
    return a_list, num_of_fruit

result = a_fruit_list()
print("List of fruits with the letter 'a':", result[0])
print("Total number of fruits with the letter 'a':", result[1])'''

list = ['Cuddly critters, koalas measure about 60cm to 85cm long, and weigh about 14', '.']
first_str = list[0]

print(first_str)

      






    





