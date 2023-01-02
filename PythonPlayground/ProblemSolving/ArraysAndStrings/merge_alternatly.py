def mergeAlternately(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    
    result_list = []

    if len(word1) >= len(word2):
        long_list = list1
        short_list = list2
    else: 
        long_list = list2
        short_list = list1
    
    for i in range(len(long_list)):
        if i > len(short_list) - 1:
            result_list.append(long_list[i])
        else:
            result_list.append(list1[i])
            result_list.append(list2[i])

    return("".join(result_list))

print(mergeAlternately("abc", "efg"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq"))