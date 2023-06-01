import logging

# 通过模块级别函数打印日志
# 通过配置方法 设置日志打印级别
import time

date = '0' + str(time.localtime().tm_mon) + str(time.localtime().tm_mday)
logging.basicConfig(filename=f'd:/log{date}.log', level=logging.INFO, format="%(levelno)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(message)s")


# 　打印日志级别
def test_logging():
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')  # 默认级别
    logging.error('Python Error')
    logging.critical('Python critical')


test_logging()
