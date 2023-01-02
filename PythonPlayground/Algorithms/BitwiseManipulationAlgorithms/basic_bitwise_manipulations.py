# Test even or odd 

def turn_off_kth_bit(n, k):
    return n & ~(1 << (k-1))

def turn_on_kth_bit(n, k):
    return n | (1 << (k-1))

def toggle_kth_bit(n, k):
    return n ^ (1 << (k-1))

def is_odd_or_even(num):
    if (num & 1) == 0:
        return(num, " is Even")
    elif (num & 1) != 0:
        return(num, " is odd")

# Test negative or positive 

def is_neg_or_pos(num1, num2):
    print(f"{num1} in binary is {bin(num1)}")
    print(f"{num2} in binary is {bin(num2)}")

    if (num1 ^ num2) < 0:
        return(f"{num1} and {num2} have opposite sign")
    else:
        return(f"{num1} and {num2} have the same sign")

# print(is_neg_or_pos(8, 2))

def swap_vars(x, y):
    if (x != y):
        print(f"x is {x} and y is {y}.")
        # x = x ^ y
        # y = x ^ y
        # x = x ^ y
        xored = x ^ y
        y = xored ^ y
        x = xored ^ x
        print(f"But after flipping them x is {x} and y is {y}")
    else:
        print("Numbers can not be equal")

# print(swap_vars(2, 5))

def unset_rightmost_bit(x):
    pass