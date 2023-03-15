# import logging

# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# print("logging demo")
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning messgage")
# logging.error("error message")
# logging.critical("critical message")


import logging
'''logging.basicConfig(filename='log.txt',level=logging.INFO)
print("Logging Module Demo")
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")'''

logging.basicConfig(filename='log2.txt',level=logging.INFO)
logging.info("A new connection came")
try:
    a=int(input(" 1 =>"))
    b=int(input("2 => "))
    print(a/b)
except ZeroDivisionError as msg:
    print("can't divide by zero")
    logging.exception(msg)
except ValueError as msg:
    print("no is required")
    logging.exception(msg)    


logging.info('request processing completed')    