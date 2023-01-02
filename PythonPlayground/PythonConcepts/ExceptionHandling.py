# Exceptions catch things you know might actually fail.
# The try block tries things then the except handles things if things go wrong. 

# Build your own exception
class MyException(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.line_number = args[1]