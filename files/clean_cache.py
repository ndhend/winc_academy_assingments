


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


clean_cache()
