
def cached_files():
    folder_path = r'C:\Users\nhend\winc\files\cache'
    cache_file_list =[]
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
    
    # Check if the item is a file
    if os.path.isfile(file_path):
        cache_file_list.append(filename)
    return cache_file_list


print(cached_files)

'''find_password: takes the list of file paths from cached_files as an argument. 
function should read the text in each one to see if the password is in there.
-> how to read files in python

there should be a word indicating password -> password

find_password(my_list) should return the password

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:  # opens and 'r' reads
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

file_path = 'path/to/your/textfile.txt'  # Replace with the actual path to your text file
text_content = read_text_file(file_path) # 

if text_content is not None:
    print(text_content)
'''