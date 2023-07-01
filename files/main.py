# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line


''' Goal: find a super secret passwor to world dominination
    This password is in a text file
    The text file is in sea text files.
    We will use Python's standard library'''



'''
#clean_cache: takes no arguments and
#creates an empty folder named cache in the current directory.
def clean_cache():
folder_name = 'cache'
    new_folder = os.makedirs(folder_name)
    return new_folder

'''

# The function clean_cache() should create an empty folder 'cache' in the current directory 
# If it already exists, delete everything in the 'cache' folder but keeps the 'cache'folder
# somehow the code keeps deleting the folder instead of just the content???


import os


def clean_cache():
    folder_path = r'C:\Users\nhend\winc\files'
    folder_name = 'cache'
    directory = os.path.join(folder_path, folder_name)
    
    # Create a folder 'cache' if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        print(f"Folder '{directory} created.")
    else:
        # Delete the contents of the folder
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"The '{directory}' was emptied.")

# clean_cache()

import zipfile


zip_file_path = r'C:\Users\nhend\winc\files\data.zip'
cache_dir_path = r'C:\Users\nhend\winc\files\cache'


def cache_zip(zip_file_path, cache_dir_path):  # (str, str)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
        # Thezipfile.ZipFile class opens the zip file in read mode ('r').
        # .extractall() method of zip-rif extracts all the contents
        # of the zip file into the cache_dir_path

    print('Zip file extracted successfully.')


# cache_zip(zip_file_path, cache_dir_path)

'''cached_files: takes no arguments

def cached_files()
    cache_file_list =[]
 and returns a list of all the files in the cache. '''


def cached_files():
    folder_path = r'C:\Users\nhend\winc\files\cache'
    cache_file_list = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            cache_file_list.append(file_path)
    return cache_file_list


cache_file_list = cached_files()
print(type(cache_file_list))

'''find_password: takes the list of file paths from cached_files as an argument. 

def find_password(my_list):

function should read the text in each one to see if the password is in there.
-> how to read files in python

there should be a word indicating password -> password

find_password(my_list) should return the password string

def find_password(file_list):
    found_password = ' '
    for file in file_list:
        with open(file_path, 'r') as file:  # opens and 'r' reads
            text = file.read()
            if 'password' in text.lower():
                found_password = text
                break
    return found_password


print(find_password(cache_file_list))'''


def find_password(file_list):
    found_password = ' '
    for file_name in file_list:
        with open(file_name, 'r') as file:  # opens and 'r' reads
            text = file.read()
            lines = text.split('\n')  # Split the text into lines
            for line in lines:
                if line.startswith('password:'):
                    found_password = line.split(':', 1)[1].strip()
                    return found_password


print(find_password(cache_file_list))
