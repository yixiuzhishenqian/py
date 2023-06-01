import logging.config
# 读取文件
logging.config.fileConfig('logger.conf')
# 从文件中获取出来已存在的logger
myLogger = logging.getLogger('ml')

myLogger.debug('this is debug log')
myLogger.info('this is info log')
myLogger.warning('this is warning log')
myLogger.error('this is error log')
myLogger.critical('this is critical log')