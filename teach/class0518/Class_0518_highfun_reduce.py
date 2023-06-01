# 将函数作为参数使用的函数就是高阶函数
# reduce
from functools import reduce


def power(x, y):
    return x + y


print(reduce(lambda x, y: x + y, list(range(6))))
