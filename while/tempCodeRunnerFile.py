def a_fruit_list():
    num_it = 0
    a_list = []
    while num_it < 1000:
        fruit = random_koala_fact()
        if 'kg' in fruit.lower():
            if fruit not in a_list:
                a_list.append(fruit)
            num_it += 1
    string = a_list[0]
    kg =  int(string.find ('kg'))
    return kg

print(a_fruit_list())