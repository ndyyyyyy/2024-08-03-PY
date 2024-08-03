# ?How to create a logger.
import logging
#logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y/%m/%d %H:%M:%S")
#logging.debug("This is a debug message!")
#logging.info("This is an info message!")
#logging.warning("This is a warning message!")
#logging.error("This is an error message!")
#logging.critical("This is a critical message!")


# ?Importing your own logger.
#print("\n")
#import Logging_hepler


# ?How to create log handlers.
#logger = logging.getLogger(__name__)

# Create a handler.
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler("file.log")

# Level and the format
#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)

#fromatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
#stream_h.setFormatter(fromatter)
#file_h.setFormatter(fromatter)

#logger.addHandler(stream_h)
#logger.addHandler(file_h)

#logger.warning("This is another Warning!")
#logger.error("This is another Error!")


# ?How to use a file config method.
#import logging.config

#logging.config.fileConfig('logging.conf')

#logger_ =logging.getLogger('simpleExample')
#logger_.debug("This is another debug message.")


# ?Capturing stack tarces(useful for trubleshooting).
#try:
#    a = [1, 2, 3]
#    val = a[4]
#except IndexError as e:
#    logging.error(e, exc_info=True)


#print("\n")
#import traceback
#try:
#    b = [4, 5, 6]
#    val1 = b[7]
#except:
#    logging.error("The error is %s", traceback.format_exc())    

# ?How to keep track of the most recent events in your file/application.
from logging.handlers import RotatingFileHandler
import time

logger__ = logging.getLogger(__name__)
logger__.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs: app.log.1, app.log.2, etc.
handler_ = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger__.addHandler(handler_)

for _ in range(10000):
    logger__.info("Hello World!")


# ?How to make a time based file rotater.
from logging.handlers import TimedRotatingFileHandler

logger_1 = logging.getLogger(__name__)
logger_1.setLevel(logging.INFO)

# What we can give as argumnets for "when": s "second", m "minute", h "hour", d "day", midnight, w0 "Monday", w1 "Tuesday"...
handler_1 = TimedRotatingFileHandler("timed_test.log", when="m", interval=5, backupCount=5)
logger_1.addHandler(handler_1)

for _ in range(6):
    logger_1.info("Hello World!")
    time.sleep(5)