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
#   - 可变参数
# *
def info3(name, *args):
    print(name)
    print(args)


info3('dahuang', 34, '男')

print("-" * 40)


def variable_fun(kind, *arguments):
    print("friend : ", kind, ";")
    print(arguments)


# 函数调用
variable_fun("xiaoming", "hello xiaoming", "nice to meet you!", 555)