'''def unique_koala_facts(n):
    # Maak variabelen aan die aangeven hoe vaak de while loop mag itereren totdat hij ermee stopt (in opdracht staat 1000)
    loop_num = 0
    max_loop = 1000
    # Maak een lijst aan waarin je je unieke feitjes in opslaat, deze lijst geef je op het eind terug
    unique_facts_list = []
    # Je blijft door je while loop gaan totdat je lengte van je unique_facts_list gelijk is aan de parameter n
    while len(unique_facts_list) < n:
        # roep een feitje op
        fact = random_koala_fact()
        # TODO: Check of het feitje al in je unique_facts_list zit, zo nee voeg hem dan toe.
        # TODO: Check of loop_num groter is dan max_loop, zo ja stop dan met je while loop HINT: break
        # TODO: Voeg eentje toe aan loop_num
    # TODO: Geef unique_facts_list terug nadat je while loop klaar is.'''

import random

def random_koala_fact():
    facts = [
        "Koalas are not bears; they are marsupials.",
        "Koalas have fingerprints similar to humans.",
        "Koalas sleep for up to 20 hours a day.",
        "Koalas eat mainly eucalyptus leaves.",
        "Koalas are native to Australia.",
    ]
    return random.choice(facts)

if __name__ == "__main__":
    fact = random_koala_fact()
    print(fact)

def unique_koala_facts(n):
    loop_num = 0
    max_loop = 1000
    unique_facts_list = []
    while len(unique_facts_list) < n:
        fact = random_koala_fact()
        if fact not in unique_facts_list:
            unique_facts_list.append(fact)
        loop_num += 1
        if loop_num >= max_loop:
            break
    return unique_facts_list

result = unique_koala_facts(1000)
print(result)
