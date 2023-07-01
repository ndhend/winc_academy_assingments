#num_joey_facts: young marsupials are called 'joeys'.

# How many unique facts mentioning this term are in our facts dataset? -> count 'joeys' count = 0, count +=1
# Count them by getting facts from random_koala_fact until -> if joeys in fact count +=1
# you have seen some particular fact 10 times -> fact = '' 
# heb gezien optellen -> hoe? if num_of_fact == 10 break
# then return how many unique joey facts you counted in the dataset -> return num_of_fact

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
            some_fact = a_list[0]
            print(some_fact)
            if fruit == some_fact:
                count +=1
            if count == 10:
                break
        num_a_facts = len(a_list)
    return num_a_facts

print(a_fruit_list())

