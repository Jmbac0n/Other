import pickle

simple_dict = {'1': 'key1', '2': 'key2', '3': 'key3'}
file_to_save = open('D:\\MyScripts\\Data_Structures\\save_dict.pkl', 'wb')
pickle.dump(simple_dict, file_to_save)
file_to_save.close()
