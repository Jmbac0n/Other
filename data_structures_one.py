# Lists

num_list = [1, 2, 3, 4, 5]
print(num_list)

num_list.append(6)
print(num_list)

num_list.insert(4, 7)
print(num_list)

num_list.remove(7)
print(num_list)

# Tuple

a_tuple = 1, 'a', 2.0, 'b'
print(a_tuple)

# Dictionary

simple_dict = {'a': 1, 'b': 2, 'c': 3}
x = input()
if x in simple_dict:
    print(simple_dict[x])
else:
    print("Not found")


# Use Cases for later projects

# Saving files into accessible list for loading in terminal
# Same but for loading encryption keys
