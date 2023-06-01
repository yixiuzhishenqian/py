def myFunc(num1, num2):
    return num1 - 1, num2 + 1


# python中的函数可以一次性返回多个值
# 默认情况下接收为一个元组
li = myFunc(2, 1)
print(li)
print(type(li))
# 也可以按照 '解构赋值' 进行返回值的接收
a, b = myFunc(2, 1)
print(a)
print(b)
