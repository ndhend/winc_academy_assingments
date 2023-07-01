# Do not modify these lines
from helpers import get_countries


__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
# OPDRACHT 1 ###############################################

countries = get_countries()
# print(type(countries))

'''We express a nationality as a country (str) from the 
list returned by get_countries.'''


def nationality(countries):
    # nationality = ''    # Default value if 'Uganda' is not in the list
    if 'Uganda' in countries:
        nationality = 'Uganda'
    return nationality


# print(nationality(countries))


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        'name': name,
        'date_of_birth': date_of_birth,
        'place_of_birth': place_of_birth,
        'height': height,
        'nationality': nationality  # Call the nationality function to get the nationality
    }
    return passport


updated_passport = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, nationality)
# print (type(updated_passport))

''' stamp -> shows that they have been to a certain country
Travellers don't need stamps of their home country.'''

list_of_countries = []


def country_stamp(selected_country):
    if selected_country not in list_of_countries:
        if selected_country != updated_passport['nationality']:
            list_of_countries.append(selected_country)
    return list_of_countries


visited_countries = country_stamp('Iran')

# print(type(visited_countries))


def add_stamp(updated_passport, visited_countries):
    updated_passport['stamps'] = visited_countries
    return updated_passport


updated_passport = add_stamp(updated_passport, visited_countries)
# print(updated_passport)


def add_biometric_data(omari,
                       biometric_data,
                       biometric_value,
                       recorded_date):
    # (dict, str, value, str)
    if 'biometric' not in omari:
        omari['biometric'] = {}
    
    omari['biometric'][biometric_data] = {
            'date': recorded_date,
            'value': biometric_value}
    return omari

# the second key "eye_color_ right" should add up as a key withiin the 'biometric' key


omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
# print(omari)

fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)





