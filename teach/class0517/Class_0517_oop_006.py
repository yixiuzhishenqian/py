# 一个类没有继承任何类的时候,默认集成Object类
class Car:
    name = 'car'

    def __init__(self, name='car'):
        self.name = name

    def run(self, speed):
        print('car ===> ', self.name, '以', speed, '速度行驶')


class jiaoche(Car):
    name = 'jiaoche'

    def __init__(self, name='jiaoche'):
        self.name = name

    # 方法的重写
    def run(self, speed):
        print('jiaoche ===> ', self.name, '以', speed, '速度行驶')


class kache(Car):
    name = 'kache'

    def __init__(self, name='kache'):
        self.name = name

    # 方法的重写
    def run(self, speed):
        print('kache ===> ', self.name, '以', speed, '速度行驶')


# 多态
def testRun(c):
    c.run(100)


# 实例化car对象
car = Car("普通汽车")
# 实例化jiaoche对象
jiaoche = jiaoche("宝马")
# 实例化kache对象
kache = kache("曼恩")

testRun(car)
testRun(jiaoche)
testRun(kache)
