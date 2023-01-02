def gen_fun1(my_list):
    for name in my_list:
        yield "_______"
        yield "Name:"
        yield name
        yield " "
    """ Run:
        for i in gen_fun1(names):
            print(i)
    """

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
    """ For loop to reverse the string
        for char in rev_str("hello"):
            print(char)
    """

# One line code for suming all numbers in a list: 
    # print(sum(x for x in list_numbers))

# Iterator Class
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# The Iterator class can be turned into a generator:
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

# Represent Infinite Stream
def all_even():
    n = 0
    while True:
        yield n
        n += 2

# If we want to find out the sum of squares of numbers in the 
# Fibonacci series, we can do it in the following way by pipelining the output of generator functions together.
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x


def square(nums):
    for num in nums:
        yield num**2

# print(sum(square(fibonacci_numbers(10))))

"""
Notes:
Yield - Pauses the function saving all the states and continues to the next calls. 
Generators have lazy execution and only create on demand. 

Advantages to using Generators:
1. Memory Efficient - A normal function to return a sequence will create the entire sequence in memory before returning the result.
This is great for a sequence that is very very large. 
2. Easier to impliment than iterator classes.
3. Can represent an infinite stream of data.  
4. Can pipeline generators together
"""