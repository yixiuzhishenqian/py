d = 0
# try里面写的是可能会发生异常的代码
# except 异常类型,可以捕获指定类型的异常
# 我们在except中编写的语句就是在处理异常,进行了处理之后,我们就可以继续执行之后的语句了(如果有)
try:
    if 2 == 2:
        # d = 5 / 0 # ZeroDivisionError
        # d = '1' + 2 # TypeError
        d = 5 + 0
    else:
        d = 5 * 0
except ZeroDivisionError:
    print('除数不能为0')
except TypeError:
    print('类型异常')
else:
    print('没有发生任何异常')
print("结果是 : ", d)
