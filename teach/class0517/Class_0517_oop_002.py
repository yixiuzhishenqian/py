class Car:
    # 类中的属性
    name = 'benz'

    # 普通方法(函数)/实例方法
    # self 是一个关键字
    # 表示 这个类的实例
    # 谁调用self就是谁
    def run(self):
        """
        :parameter: None
        :return: None
        """
        print(self)
        print(self.name, "is running")


# 第一次实例化 Car() 0x000001B99B4DECD0
# 把对象赋值给car这个变量
car1 = Car()
print("car1", car1)
# 第二次实例化 0x000001B99B4D5D90
# 没有给变量赋值
car2 = Car()
print("car2", car2)

# 使用类中的属性
# 对象.属性
print("car1", car1.name)
print("car2", car2.name)
car1.name = '宝马'
# car2.name = '奔驰'
# 调用实例(对象)方法,先有对象才能使用
car1.run()
car2.run()
