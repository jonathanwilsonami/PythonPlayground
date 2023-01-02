import logging
import logging.config

logging.config.fileConfig('logging.conf')

################ Root Logger: ##############
# Does basic config for the logging system by creating a StreamHandler with a default Formatter and adding it to the root logger. 
# Functions such as debug() will call basicConfig() automatically if no handlers are defined for the root logger. 
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

############## For logging in different modules. Creates your own logger that is not tied to the root logger. ##############
# __name__ will be the name of the module that it is in. 
# logger = logging.getLogger(__name__)

############## Propogation - By default, all created loggers will pass the log events to the handlers of higher loggers, in addition to any handlers attached to the 
# created logger. You can deactivate this by setting propagate = False. Sometimes when you wonder why you don't see log messages from another module, 
# then this property may be the reason.

# logger.propagate = False

logging.debug('This is a debug message')

# Log handlers
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log') # file.log will be added 

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR) 

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning!')

#################### Output config methods 

logger = logging.getLogger('simpleExample')

################## Caputuring stack traces ##############

# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True) # print the stack trace

# OR

# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error("This is an error %s", traceback.format_exc()) # print the stack trace

############## Rotating file handler ##############

from logging.handlers import RotatingFileHandler

# When logs get more that 2000 bytes create a new log file up to 5 
# RotatingFileHandler supports log file rotation, which gives the handler the ability to rotate log files based on its maximum size. 
# 2 parameters should be defined here: maxBytes and backupCount. maxBytes tells the handler when to rotate the log.
# When you have a large application that logs many events to a file, and you only need to keep track of the most recent events, then use a RotatingFileHandler 
# that keeps the files small. When the log reaches a certain number of bytes, it gets "rolled over". You can also keep multiple backup log files before overwriting 
# them.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

############## TimedRotatingFileHandler ##############
# If your application will be running for a long time, you can use a TimedRotatingFileHandler. This will create a rotating log based on how much time has passed. 
# Possible time conditions for the when parameter are: sec, min, hour, day, w0-w6 (0=Monday), midnight.

# from logging.handlers import TimedRotatingFileHandler

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
# handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
# logger.addHandler(handler)