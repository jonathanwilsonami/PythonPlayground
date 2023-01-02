# Collection of tools for handinling iterators. Iterators or anything that can be iterated. For example a list. 
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat 
import operator

a = [1, 2]
b = [3, 4]

prod = product(a,b) # Computs the cartesian product
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

# Return all possible orderings of an input
a = [1,2,3]
perm = permutations(a)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

b = list('abc')
perm2 = permutations(b)
# perm2 = permutations(b, 2) # Give permutations with length of 2
print(list(perm2)) # 

# Combination will make all possible cobinations with a specified length.  
x = [1,2,3,4]
comb = combinations(x, 2)
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb2 = combinations_with_replacement(x, 2)
print(list(comb2)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# Accumulate - makes an iterator that returns accumulated sums or any other binary function given as input. 
acc = accumulate(x)
print(list(acc)) # [1, 3, 6, 10]

acc2 = accumulate(x, func=operator.mul) # Multiply accumulate 
print(list(acc2)) # [1, 2, 6, 24]

# Find max in list
m = [1,2,3,5,3,1,3,1,1,67,1,1,2,34,100] 
acc3 = accumulate(m, func=max)
print(list(acc3)) # [1, 2, 3, 5, 5, 5, 5, 5, 5, 67, 67, 67, 67, 67, 100]

# Groupby - makes an iterator that returns keys and groups from an inner iterable. 

def larger_than_f(letter):
    return letter > 'f'

letters = ['a', 'b', 't', 'z', 'f'] 
group_obj = groupby(letters, key=larger_than_f)
# Doing this with a lambda - group_obj = groupby(letters, key=lambda x: x>'f')
for key, val in group_obj:
    print(key, list(val)) # False ['a', 'b'], True ['t', 'z']

# Group persons by age
persons = [{'name': 'Tim', 'age': 24}, {'name': 'James', 'age': 24}, {'name': 'John', 'age': 26}, {'name': 'Joe', 'age': 21}, {'name': 'Lauren', 'age': 21}]

group_by_obj = groupby(persons, key=lambda x: x['age'])
for key, val in group_by_obj:
    print(key, list(val))
# 24 [{'name': 'Tim', 'age': 24}, {'name': 'James', 'age': 24}]
# 26 [{'name': 'John', 'age': 26}]
# 21 [{'name': 'Joe', 'age': 21}, {'name': 'Lauren', 'age': 21}]

# Infinite iterators 

# count infinitly starting at 10
for i in count(10):
    print(i)
    if i == 25:
        break

# Infinitly cycle through numbers 
a = [1,2,3]

# for i in cycle(a):
#     print(i)

# for i in repeat(1):
#     # Just repeat 1 over and over
#     print(i)

for i in repeat(1, 10):
    # Repeat 1 for 10 times
    print(i)