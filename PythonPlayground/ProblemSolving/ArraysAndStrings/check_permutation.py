# Ask what chars will be used. ASCII? Unicode? And are the chars case sensitive. 

def check_permutation_with_sort(str1, str2):
    str1_chars = list(str1)
    str2_chars = list(str2)
    if len(str1_chars) is not len(str2_chars):
        return(False)

    elif sorted(str1_chars) == sorted(str2_chars):
        return(True)
    else:
        return(False)

# print(check_permutation_with_sort("dog", "god"))
# print(check_permutation_with_sort("abc", "ab")) 
# print(check_permutation_with_sort("dog", "abc"))


def check_permutation(str1, str2):
    str1_chars = list(str1)
    str2_chars = list(str2)
    if len(str1_chars) is not len(str2_chars):
        return(False)

    s_dict = {}
    for c in str1_chars:
        if s_dict.get(c):
            s_dict[c] = s_dict.get(c,0) + 1 
            # print(s_dict[c]) 
        else:
            s_dict[c] = 1
    for c in str2_chars:
        s_dict[c] = s_dict.get(c,0) - 1
        if s_dict.get(c) < 0:
            return(False)
        
    return(True)

# print(check_permutation("dog", "god"))
# print(check_permutation("doooggg", "doooggg"))
# print(check_permutation("dog", "abc"))
# print(check_permutation("abc", "ab")) 


    