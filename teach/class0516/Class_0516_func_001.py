# 重复去做某一件事,需要多次编写代码,使用函数,可以编写一次代码,然后反复嗲用函数,就能达到之前的效果
# def 函数名(参数):
#    函数体

# 创建一个计算绝对值的函数
# return 返回数据之外 还可以中断函数的运行
def myabs(a, b):
    print(a)
    print(b)
    num = int(input("输入一个数字"))
    if num < 0:
        return -num
    return num
    # print("不会被执行的语句")


myabs(1, 2)
myabs(2, 3)
myabs(3, 4)
myabs(4, 5)
# if num < 0:
#     print(-num)
# else:
#     print(num)
#
# num1 = int(input("输入一个数字"))
# if num1 < 0:
#     print(-num1)
# else:
#     print(num1)
#
# num2 = int(input("输入一个数字"))
# if num2 < 0:
#     print(-num2)
# else:
#     print(num2)
#
# num3 = int(input("输入一个数字"))
# if num3 < 0:
#     print(-num3)
# else:
#     print(num3)
