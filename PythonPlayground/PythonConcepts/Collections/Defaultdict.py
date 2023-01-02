from Collections import Defaultdict

# Helps us avoid a key error
d = Defaultdict(float)

d['a'] = 1.0
d['b'] = 2.0

print(d['c']) # will print the default which is zero or 0.0

# c = Defaultdict(list)

