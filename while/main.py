from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    random_koala_fact()
unique_fact = random_koala_fact()
#print(unique_fact)

########################## OPDRACHT 1#######################################################################
# unique_koala_facts: takes an integer as an argument and returns that number of unique koala facts in a list.
# You can set an iteration limit of 1000.
# random_koala_fact is defined
'''def unique_koala_facts(n):
    # Maak variabelen aan die aangeven hoe vaak de while loop mag itereren totdat hij ermee stopt 
    # (in opdracht staat 1000)
    loop_num = 0
    max_loop = 1000
    # Maak een lijst aan waarin je je unieke feitjes in opslaat, deze lijst geef je op het eind terug
    unique_facts_list = []
    # Je blijft door je while loop gaan totdat je lengte van je unique_facts_list gelijk is aan de 
    # parameter n -> 1000
    while len(unique_facts_list) < n:
        # roep een feitje op
        unique_fact = random_koala_fact()
        if unique_fact not in unique_facts_list:
            unique_facts_list.append(unique_fact)
            loop_num += 1 
        if loop_num == max_loop:
            break
        count = len(unique_facts_list)
    return count     
                    
print(unique_koala_facts(1000))'''


def unique_koala_facts(n):
    loop_num = 0
    max_loop = 1000
    unique_facts_list = []

    while len(unique_facts_list) < n:
        unique_fact = random_koala_fact()
        if unique_fact not in unique_facts_list:
            unique_facts_list.append(unique_fact)
        loop_num += 1
        if loop_num == max_loop:
            break
        #count = len(unique_facts_list)
    return unique_facts_list # Winc want the list of facts not the number of facts
print(unique_koala_facts(1000)) #Output: 29


################################ OPDRACHT 2##################################################################

#num_joey_facts: young marsupials are called 'joeys'.
#How many unique facts mentioning this term are in our facts dataset?
#Count them by getting facts from random_koala_fact until you have seen some particular fact 10 times 
#return how many unique joey facts you counted in the dataset.

def num_joey_facts():
    num_it = 0
    joey_list = []
    count = 0
    while num_it < 1000:  
        joey_fact = random_koala_fact()
        if 'joey' in joey_fact:
            if joey_fact not in joey_list:
                joey_list.append(joey_fact)
            num_it += 1
            some_fact = joey_list[0]
            if joey_fact == some_fact:
                count +=1
            if count == 10:
                break
        num_of_facts = len(joey_list) 
    return num_of_facts

print(num_joey_facts ())

################################ OPDRACHT 3 ################################################################

'''koala_weight: somewhere in the data is a fact about how heavy a koala is. 
This function should return that weight in kilogram (kg) as an integer'''

def koala_weight():
    # num_it = 0
    # koala_weight_list =[] # koala_weight_str = ' ' . koala_weight_str = str()
    weight = random_koala_fact()
    while 'kg' not in weight:
        weight = random_koala_fact()
        print (weight)
        # if 'kg'in weight.lower():
            #break
            #if weight not in koala_weight_list:
                #koala_weight_list.append(weight) # kan je niet gewoon een string uit de lijst halen?
        '''num_it += 1''' 
        kg = weight.split('kg')
        kg_0 = kg[0]
        print (kg_0)
        kg_list = kg_0.split(' ')
        print (kg_list)
        num_kg = kg_list[-1]

        
    return (int(num_kg))
    '''koala_words = koala_str.split()
    for word in koala_words:
        if 'kg' in koala_words:
           print(word) # ik weet niet wat ik moet doen om int: 14 te krijgen
           # num_kg = word[:-2] werkt niet????
           # Output: UnboundLocalError: cannot access local variable 'num_kg' 
           # where it is not associated with a value
    #return weight'''
print(koala_weight()) # Output : 14kg


