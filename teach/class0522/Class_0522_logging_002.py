import logging
import time


def getLog():
    # 获取logger
    myLogger = logging.getLogger('ml')
    # 设置日志输出级别
    myLogger.setLevel(logging.INFO)
    date = '0' + str(time.localtime().tm_mon) + str(time.localtime().tm_mday)
    # 实例化日志处理器
    fileHandler = logging.FileHandler(f"d:/log{date}.log")

    # 实例化格式化实例
    defaultFormat = logging.Formatter(
        fmt="%(levelno)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(message)s", datefmt=None)
    # 添加格式
    fileHandler.setFormatter(defaultFormat)

    # 添加日志处理器
    myLogger.addHandler(fileHandler)

    # 实例化过滤器
    defaultFilter = logging.Filter(name='')
    # 添加过滤器
    myLogger.addFilter(defaultFilter)
    return myLogger


# myLogger = getLog()
# myLogger.debug('this is debug log')
# myLogger.info('this is info log')
# myLogger.warning('this is warning log')
# myLogger.error('this is error log')
# myLogger.critical('this is critical log')
