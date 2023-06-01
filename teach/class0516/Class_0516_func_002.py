# 声明
# 无参数,无返回值函数
def info():
    print("我叫大黄,今年34岁")


# 有参数,无返回值函数
# name 形式参数 形参
def show(name):
    print(f"我叫{name},今年34岁")


# 无参数,有返回值函数
def myinfo():
    return "我叫大黄,今年34岁"


# 有参数,有返回值函数
def myshow(name):
    return f"我叫{name},今年34岁"


# 调用
# 调用,无参数,无返回值函数
info()
# 调用,有参数,无返回值函数
# aaa 实际参数 实参
aaa = 'dahuang'
show(aaa)
# 调用,无参数,有返回值函数
funcReturn1 = myinfo()
print(funcReturn1)
# 调用,有参数,有返回值函数
funcReturn2 = myshow('dahuang')
print(funcReturn2)
