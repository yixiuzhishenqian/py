# 将函数作为参数使用的函数就是高阶函数
# map
def power(num):
    return num ** 2


def hf1(fun, array):
    return [fun(x) for x in array]


print(list(map(power, list(range(10)))))
