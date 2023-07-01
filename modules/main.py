# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# import this

# print(this)

'''Write a function wait that takes one argument -- seconds (int) --

def wait(seconds): # int
    time.sleep(seconds)
    return ' '
    


that uses a function in the time module 


to make the computer wait for that number of seconds, 
then returns nothing.'''


import time

# print(dir(time))

def wait(seconds): # int
    time.sleep(seconds)
    return ' '

# print(wait(10))

'''Implement a function my_sin that takes one float as an argument 
and returns the sine (sinus) of that float. Use the math module.'''

import math

# print(dir(math))


def my_sin(fl_arg): 
    return math.sin(fl_arg)


# print(my_sin(0.5))


from datetime import datetime  # get datetime class from the datetime module


# Get the current date and time
# current_datetime = datetime.now()

# Format the datetime object in ISO 8601 format
# iso_formatted_datetime = current_datetime.isoformat(timespec='minutes')

# print("Current date and time (ISO 8601 format):", iso_formatted_datetime)

# print(dir(datetime))


def iso_now():
    current_datetime = datetime.now() # use method .now() for current date and time
    iso_formatted_datetime = current_datetime.isoformat(timespec='minutes') # use method .isoformat()
    # timespec='minutes'argument: displayinig up to minute precision
    return iso_formatted_datetime


# print(iso_now())

import sys


def platform():
    current_platform = sys.platform
    return current_platform

    
print(platform()) # Output win32

from greet import supergreeting as supergreeting_wrapper

print(supergreeting_wrapper('Alice'))









