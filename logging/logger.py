# by default the logger is set to root so we can create a new logger

import logging

newLogger = logging.getLogger(__name__)
# create a new logger with the name of the module
newLogger.propagate=False
newLogger.info("Hello from newLogger ")

# rotating file handler 
# if our application is running with a lot of log messages we can implement this to manage our log file size

from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
import time
newLogger.setLevel(logging.INFO)

# roll over after 2KB and keep backup logs 

rotatingHandler=RotatingFileHandler('app.log',maxBytes=2000,backupCount=5)
# this creates a log based on how much time has passed 
# seconds(s),minutes(m),hours(h),
timeHandler=TimedRotatingFileHandler('time.log',when='s',interval=1,backupCount=5)
newLogger.addHandler(rotatingHandler)
newLogger.addHandler(timeHandler)

# for _ in range(20000):
#     newLogger.info("logging through")

for _ in range(6):
    newLogger.info("logging through timeer")
    time.sleep(5)