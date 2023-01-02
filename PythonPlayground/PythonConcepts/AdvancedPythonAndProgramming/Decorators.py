# Functions are first class objects in Python. 


def add_header(fun):
    def string_gen(*args, **kwargs):
        print("****************")
        fun(*args, **kwargs)
        print("****************")
    return string_gen

def capitalize_string(fun):
    def string_gen(*args, **kwargs):
        fun((args[0].upper()))
    return string_gen

def add_undersores(fun):
    def string_gen(*args, **kwargs):
        fun((args[0].replace(" ", "_")))

    return string_gen

@add_header
@capitalize_string
@add_undersores
def print_string(my_string):
    print(my_string)

# print_string("Testing one two")