def replace_spaces(str):
    char_list = list(str)
    url_ifed_list = []
    for i in range(len(char_list)):
        if char_list[i] == ' ':
            url_ifed_list.append('%')
            url_ifed_list.append('2')
            url_ifed_list.append('0')
        else:
            url_ifed_list.append(char_list[i])
    print(''.join(url_ifed_list))
            

    print(char_list)

replace_spaces('abc bc   ')

# test_str = "aaa fff aaaa   "
