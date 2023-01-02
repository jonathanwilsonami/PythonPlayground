#O(nlog(n))

def check_unique(x, y):
    letters = {}

    for c in x:
        letters[c] = letters.get(c, 0) + 1
        print(letters[c])
    
    for c in y: 
        letters[c] = letters.get(c, 0) - 1
        
        if (letters[c] < 0):
            print("Is not unique")
            return
    print("Is unique!")
    return 

check_unique("aab", "aab")
check_unique("abcd", "abc")