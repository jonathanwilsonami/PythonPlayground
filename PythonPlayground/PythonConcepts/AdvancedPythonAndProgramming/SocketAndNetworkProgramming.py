# TCP connections/Sockets 
# An Internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network.
# # Ports ar application-specific or process-specific software comunnications endpoint. It allows multiple networked applications to coexist on the same server. 
import socket

# Below is a veryy simple web browser using Socket 

# the socket() function returns a socket object whose methods implement the various socket system calls.
# class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
# AF_INET is the Internet address family for IPv4. 
# SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network. 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 443))

# The opposite method of bytes.decode() is str.encode(), which returns a bytes representation of the Unicode string, encoded in the requested encoding.
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    # receive 512 chars at a time
    # Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified 
    # by bufsize (512). See the Unix manual page recv(2) for the meaning of the optional argument flags; it defaults to zero.
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    # one can create a string using the decode() method of bytes. This method takes an encoding argument, such as UTF-8, and optionally an errors argument.
    print(data.decode())
mysock.close()


# Using urllib - This does all the socket work for us. 

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())

# Web scraping 
# Be careful what sites you get data from

# Beautiful Soup - nice for doing string searches. Helps with parsing HTML. 


#### Resources
# https://docs.python.org/3/library/socket.html