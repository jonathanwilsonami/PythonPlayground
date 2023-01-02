#*args and *kwargs
# - used to pass a variable number of arguments to a function

def my_fun(a, b, *args, **kwarg):
    print('a = {0}, b = {1}'.format(a,b))
    
    if len(args) != 0:
        for i in range(len(args)):
            print(args[i])
    print()
    for (keyword, value) in kwarg.items():
        print(keyword, value)
    print()

# my_fun('1', '2')
# my_fun('1', '2', 33)

my_args = [1,2,3,4,5,55]
my_kwargs = {'name': 'ddd', 'rank': 23}

my_fun("a", "b", *my_args, **my_kwargs)

