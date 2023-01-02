# Print ASCII number. Ordinal position. 
print(ord('H'))

# Unicode
# UTF-16 - Fixed length - 2 bytes
# UTF-32 - Fixed length - 4 bytes 
# UTF-8 - 1-4 bytes. Best standard for moving data across the internet 
# b'www' is bytes type
# 'my string' is a str type. All strings internally are Unicode. 

my = 'abc123'.encode()
print(my)
print(my)
print(my.decode())