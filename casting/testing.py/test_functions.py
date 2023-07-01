# function greet that returns string 'Hello {name}
'''def greet(name):
    greet_name = f'Hello {name}!'
    return greet_name
# print (greet('Bob'))

# function add takes three numbers (integers or floats) and returns their sum
def add(x,y,z):
    add_num = x + y + z
    return add_num
# print(add(1,2,3))

# positive: takes a number (integer or float) 
# and returns whether or not it is positive in the form of a boolean
# ternary operator
def negative(x):
    if x < 0:
        return True
    else:
        return False

print (negative(0))'''

students = [
    {
        "name": "Ali",
        "family_name": "Khan",
        "skills": {
            "Python": "beginner",
            "JavaScript": "expert",
        },
        "certificates": [
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "",
            },
        ],
    },
    {
        "name": "Jessica",
        "family_name": "van Alphen",
        "skills": {
            "Python": "advanced beginner",
            "JavaScript": "beginner",
        },
        "certificates": [
            {
                "name": "Front-end Development",
                "date_of_completion": "",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "2020-01-17",
            },
        ],
    },
]

# print(students[1]["name"])  # "advanced beginner"
# print(students[1]["certificates"][0]["name"])  # Front-End Development


def f(qty=6, item='bananas', price=1.74):

    print(f'{qty} {item} cost ${price:.2f}')



