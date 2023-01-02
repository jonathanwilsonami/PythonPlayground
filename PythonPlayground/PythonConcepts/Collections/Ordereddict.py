from Collections import Ordereddict

ordered_dict = Ordereddict()
# As of Python 3.7 you can also have this using the regular dict so ordered_dict = {} also works. 

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict) # Print the dict in the order that you inserted the values. 