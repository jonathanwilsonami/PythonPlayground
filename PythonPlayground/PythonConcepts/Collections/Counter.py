# Counter is an unordered collection where elements are stored as Dict keys and their count as dict value. Counter elements count can be positive, zero or negative 
# integers. However there is no restriction on it’s keys and values. Although values are intended to be numbers but we can store other objects too.

from collections import Counter 

a = "aaaabbbbbccccccccc"
my_counter = Counter(a)
# Return a dict that contains the number of occurances of the letter in a
print(my_counter) # Ex: Counter({'c': 9, 'b': 5, 'a': 4})

print(my_counter.items()) # dict_items([('a', 4), ('b', 5), ('c', 9)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])
print(my_counter.values()) # dict_values([4, 5, 9])
print(my_counter.most_common(1)) # See most common [('c', 9)]
print(my_counter.most_common(1)[0][0]) # To get that most common element.
print(my_counter.most_common(2)) # See 2 most common [('c', 9), ('b', 5)]
print(my_counter.elements()) # Return and iterable 
print(list(my_counter.elements()))
