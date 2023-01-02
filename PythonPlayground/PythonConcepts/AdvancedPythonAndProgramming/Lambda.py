# filter and lambdas
def get_attendents_older_than_20(my_tuple):
    return(list(filter(lambda x: x[1] > 20, my_tuple)))

# Get all the evens in an varyied nested list - filter and lambdas 
def get_evens_in_nested_list(my_list):
    return [list(filter(lambda x: x%2 ==0, sub_list)) for sub_list in my_list]
    # print(get_evens_in_nested_list(variable_len_list))

# Cube the list - map and lambdas
def cube_the_list(list_1):
    cubed = map(lambda x: pow(x,3), list_1)
    return(list(cubed))

create_dict_entry = lambda name,age: {name:age}

def cal(x,y,op=lambda x,y:x**y):
    print(x,y,op(x,y))
    #Usage: cal(10,4,oops=lambda x,y:x**y)