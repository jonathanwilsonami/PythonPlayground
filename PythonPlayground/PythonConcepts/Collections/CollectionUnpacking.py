def merge_2_dicts(dict_1, dict_2):
    return {**dict_1, **dict_2}

def flip_body(my_iterable):
        if len(my_iterable) == 0:
            print("Empty iterable")
            return
        elif len(my_iterable) == 1:
            print("Only one item")
            return 
        elif len(my_iterable) == 2:
            first, last = my_iterable
            print(last, first)
            return
        first, *body, last = my_iterable
        print(first)
        body_reversed = list(reversed(body))
        print(body_reversed)
        print(last)

def looping_nested_tuples(my_nested_tuple):
    for index, (name, age) in enumerate(my_nested_tuple):
        print(index)
        print(name, age)

def my_middle(*args):
    #if even then take the average of the two numbers
    if len(args) % 2 == 0:
        left_middle_index = (len(args)//2) - 1
        middle_sum = args[left_middle_index] + args[left_middle_index + 1]
        return middle_sum/2
    else:
        middle_index = len(args) // 2
        return args[middle_index]