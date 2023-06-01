class Car:
    # 类中的属性 : 被该类所有的实例共享
    name = 'benz'

    @classmethod
    def run(cls, speed):
        print(cls.name, speed, '行驶')

    # 类中的函数
    @staticmethod
    def back():
        print('back')

# Car.name = '宝马'
# 访问
car1 = Car()
print(car1)
print(car1.name)
Car.run('100')

car2 = Car()
print(car2)
print(car2.name)
car2.run('20')

car1.back()
Car.back()