import shutil, os, pickle
from cryptography.fernet import Fernet

# Load pickle file with string names

key_name_file = 'D:\\MyScripts\\Data_Structures\\Pickle\\keys.pkl'
key_file_dest = 'D:\\MyScripts\\Data_Structures\\Pickle\\Keys'
key_file_source = 'D:\\MyScripts\\Data_Structures\\Pickle\\'

key_name = input()

keys = []


# Saves name of string into seperate pickle folder

def write_key(key_file, keyname, key_list):

    with open(key_file, 'rb') as rfp:
        key_list = pickle.load(rfp)

    new_key = keyname
    key_list.append(new_key)

    with open(key_file, 'wb') as wfp:
        pickle.dump(key_list, wfp)

# Write Key

    key = Fernet.generate_key()

    with open(keyname, 'wb') as key_file:
        key_file.write(key)

# Moves encryption key into correct file

def move_keys(keyname):

    source = key_file_source + (str(keyname))
    dest = key_file_dest

    shutil.move(source, dest)
    
# Load Key

def load_keys(keyname):

    key_name = keyname

# View Keys

def view_keys(key_file):

    with open(key_file, 'rb') as rfp:
        key_list = pickle.load(rfp)
        print(key_list)

# Main function for UI and calling of of other functions

# 1. Write Key
# 2. Load Key
# 3. View Keys

write_key(key_name_file, key_name, keys)
move_keys(key_name)
view_keys(key_name_file)