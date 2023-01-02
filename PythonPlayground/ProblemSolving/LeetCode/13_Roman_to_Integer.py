def romanToInt(s):
    roman_numeral_to_int = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    my_integer = 0

    for i in range(len(s)):
        if i+1 < len(s) and roman_numeral_to_int[s[i]] < roman_numeral_to_int[s[i+1]]:
            my_integer -= roman_numeral_to_int[s[i]]
        else:
            my_integer += roman_numeral_to_int[s[i]]

    return(my_integer)


# This is a mess! I'm leaving it though to remind me of where I used to be. 

def romanToInt2(s):
    roman_numerals = list(s)
    my_integer = 0

    i = 0
    while i < len(roman_numerals):
        if roman_numerals[i] == "I":
            if i != len(roman_numerals) - 1 and roman_numerals[i+1] == "V":
                my_integer += 4
                i += 1
            elif i != len(roman_numerals) -1 and roman_numerals[i+1] == "X":
                my_integer += 9
                i += 1
            else:
                my_integer += 1
        elif roman_numerals[i] == "V":
            my_integer += 5
        elif roman_numerals[i] == "X":
            if i != len(roman_numerals) - 1 and roman_numerals[i+1] == "L":
                my_integer += 40
                i += 1
            elif i != len(roman_numerals) - 1 and roman_numerals[i+1] == "C":
                my_integer += 90
                i += 1
            else:
                my_integer += 10
        elif roman_numerals[i] == "L":
            my_integer += 50
        elif roman_numerals[i] == "C":
            if i != len(roman_numerals) - 1 and roman_numerals[i+1] == "D":
                my_integer += 400
                i += 1
            elif i != len(roman_numerals) - 1 and roman_numerals[i+1] == "M":
                my_integer += 900
                i += 1
            else:
                my_integer += 100
        elif roman_numerals[i] == "D":
            my_integer += 500
        elif roman_numerals[i] == "M":
            my_integer += 1000

        i += 1
    return(my_integer)



# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

s1 = "III"
singleI = "I"
s2 = "LVIII"
s3 = "MCMXCIV"
s4 = "IV"
s5 = "IX"
s6 = "M"
s7 = "XL"
s8 = "CM"
s9 = "XC"

print(romanToInt(s1)) # 3
print(romanToInt(singleI)) # 1
print(romanToInt(s2)) # 58 
print(romanToInt(s3)) # 1994
print(romanToInt(s4)) # 4
print(romanToInt(s5)) # 9
print(romanToInt(s6)) # 1000
print(romanToInt(s7)) # 40
print(romanToInt(s8)) # 900
print(romanToInt(s9)) # 90
