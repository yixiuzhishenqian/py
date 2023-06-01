# 函数的参数
# 1.形参和实参名称不强制要求一致
# 2.多个参数(形参或实参)之间使用逗号分隔
# 3.参数分为
#   - 普通参数
# 不传不行
def info1(name):
    print("普通参数 : ", name)


#   - 默认参数
# =
def info2(name='dahuang'):
    print("具有默认值的参数 : ", name)


#   - 可变参数
#   - 关键字参数

info1('123')
info2()


# def demo(num, li=[]):
#     li.append(num)
#     return li
#
# print(demo(1))
# print(demo(2))
# print(demo(3))

def demo(num, li=None):
    if li is None:
        li = []
    li.append(num)
    return li


print(demo(1))
print(demo(2))
print(demo(3))
