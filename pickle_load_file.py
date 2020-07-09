import pickle

file_to_load = open('D:\\MyScripts\\Data_Structures\\save_dict.pkl', 'rb')
dict_file = pickle.load(file_to_load)

print(dict_file)