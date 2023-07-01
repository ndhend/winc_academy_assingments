# alphabet_set: takes a list of country names  takes a list def blablabla(mylist):
# and returns a list ->empty list
# of country names whose letters  -> letters
# can be combined to form the complete alphabet -> alphabet: 'abcdefghijklmnopqrstuvwxyz'

test_list = [ 'Chad', 'Gentin', 'jerusalem', 'irun', 'iarq', 'best']
def alphabet_set(my_list):
    alphabet_list = []
    for name in  my_list:
        for letter in name:
            if letter in 'abc': # elke keer een letter halen uit 'abc'
             alphabet_list.append(name)
             print 

                
    return alphabet_list
print(alphabet_set(test_list))



            




