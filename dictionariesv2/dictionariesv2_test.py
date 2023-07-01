countries = get_countries()
# print(countries)

'''We express a nationality as a country (str) from the 
list returned by get_countries.'''


def nationality(countries):
    if 'Uganda' in countries:
        nationality = 'Uganda'
    return nationality


# print(nationality(countries))


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = dict(
        name=name,
        date_of_birth=date_of_birth,
        place_of_birth=place_of_birth,
        height=height,
        nationality=nationality)
    return passport


# print(create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda"))

''' stamp -> shows that they have been to a certain country'''


def country_stamp(selected_country):
    list_of_countries = []
    if selected_country in countries: 
        if selected_country not in list_of_countries:
            list_of_countries.append(selected_country)
    return list_of_countries


stamp = country_stamp('Uganda')


def add_stamp(passport, country):
    passport['stamps'] = country_stamp(country)
    return passport
