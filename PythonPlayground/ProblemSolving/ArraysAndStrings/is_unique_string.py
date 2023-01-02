
# Time - O(n) but O(1) if the set of chars is finite i.e. ascii chars
def is_string_unique(str): 
    char_list = list(str)
    char_dict = {}
    for i in range(len(char_list)):
        if char_dict.get(char_list[i]) is True:
            return(False)
        char_dict[char_list[i]] = True
    return(True)

def is_string_unique_bitwise(str):
    checker = 0
    for i in range(len(str)):
        val = ord(str[i]) - ord("a")
        if ((checker & (1 << val)) > 0):
            return(False)
        else:
            checker |= (1 << val)
    return(True)

# print(is_string_unique("test")) # False
# print(is_string_unique("abc")) # True
# print(is_string_unique("aab")) # False
# print(is_string_unique("youare")) # True


print(is_string_unique_bitwise("test")) # False
print(is_string_unique_bitwise("abc")) # True
print(is_string_unique_bitwise("aab")) # False
print(is_string_unique_bitwise("youare")) # True
