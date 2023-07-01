test_list = [ 'chad', 'argentina', 'jerusalem', 'iran', 'iraq', 'test']
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

        
print(most_vowels(test_list))
          