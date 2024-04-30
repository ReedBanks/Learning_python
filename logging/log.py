import logging as lg

# we can log to 5 different log levels. They indicate the severity of the event
# debug, info, warning,error,critical

# re-configuring the debug level logging to print debug messages
lg.basicConfig(level=lg.DEBUG,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",datefmt="%m/%d/%y %H:%M:%S" )


# lg.debug("This is a debug message")
# lg.info("This is a info message")
# lg.warning("This is a warning message")
# lg.error("This is a error message")
# lg.critical("This is a critical message \n")

import logger

# Log handlers are responsible for dispatching the appropriate log messages to the appropriate destinations

handler = lg.getLogger(__name__)


stream_handler =lg.StreamHandler()
file_h=lg.FileHandler('file.log')

# level ,format of handlers
stream_handler.setLevel(lg.WARNING)
file_h.setLevel(lg.ERROR)

formatter=lg.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_h.setFormatter(formatter)

handler.addHandler(stream_handler)
handler.addHandler(file_h)

# lg.warning("This is a warning")
# lg.error("This is a error")

# capturing stack traces in logs
try:
    ni=[1,2,3]
    val=ni[5]
except IndexError as e:
    lg.error(e,exc_info=True)#this will include the stack trace in  our order of
    # print(e)
    
