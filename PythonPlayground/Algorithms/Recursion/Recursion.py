

# Write a recursive function that takes a number and returns the sum of all 
# the numbers from zero to that number.
def recursive_1(num):
    if num in [0, 1]:
        return num
    else:
        return num + recursive_1(num-1)

# Generator alternative
def recursive_1_gen(num):
    def recur_generator(num):
        if num in [0, 1]:
            return num
        else:
            x = 0
            y = 1
            for _ in range(num):
                x, y = y, x+y
                yield x
    *_, last = recur_generator(10)
    return last

# Factorial 
def recursion_2(num):
    if num in [0,1]:
        return 1
    else:
        return num * recursion_2(num-1)
    

# Generator alternative