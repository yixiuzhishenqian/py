# 将函数作为参数使用的函数就是高阶函数
# filter

def power(x):
    if x % 2 != 0:
        return True
    return False


print(list(filter(power, list(range(20)))))
