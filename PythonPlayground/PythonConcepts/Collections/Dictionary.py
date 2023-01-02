# A Python Dictionary is an unordered collection of data values, used to store data values like a map, which, unlike 
# other data types which hold only a single value as an element.
# Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimized. 
# In other languages a dict is called an associative array, hashmap or map. 

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict() to convert to a dict
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
# print(my_dict.get('address'))
# Check the key by using
# if 'my_key' in my_dict:
# or
# try: 
    # print(my_dict['my_key])
#except KeyError:


# KeyError
# print(my_dict['address'])

# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove last item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# # Throws Error
# print(squares)

# # Dictionary Comprehension
# squares = {x: x*x for x in range(6)}

# print(squares)

# # Dictionary Comprehension with if conditional
# odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

# print(odd_squares)

# # Membership Test for Dictionary Keys
# squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# # Output: True
# print(1 in squares)

# # Output: True
# print(2 not in squares)

# # membership tests for key only not value
# # Output: False
# print(49 in squares)

# Looping 
post = {'message': 123, 'name': 'tess'}
for key in post.keys():
    val = post[key]

for key, value in post.items():
    print(key, value)

#post.values()

# Making copies 
new_dict = my_dict.copy()
new_dict2 = dict(post)

# Merging dicts
merged_dict = new_dict.update(new_dict2)
