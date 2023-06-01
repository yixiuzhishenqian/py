from class0522.Class_0522_logging_002 import getLog

myLogger = getLog()


def plus(a, b):
    c = a + b
    s = f'a + b = {c}'
    myLogger.info(s)
    return c


plus(2, 3)
