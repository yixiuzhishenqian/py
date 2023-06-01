# 昨日回顾
# 1. 类
    # 类是对象的抽象
    # 是一个蓝图 是一个模板
    # 具有相同的特征和行为
    # 车 人 武器
# 2. 对象
    # 对象是类的实例化
    # 对象是从类中派生出来的某一个具体的事物
    # 三轮车 宝马 小明 小红 AK47 青龙偃月刀
# 3. 如何使用
# 3.1 类的声明
"""
    class 类名:
        pass
"""
# 3.2 类的实例化
"""
    变量名 = 类名()
"""
# 3.3 调用属性或方法
"""
    变量名.属性名
    变量名.方法名()
"""
# 3.4 需要注意的细节
# 每一次实例化对象{类名()} 都会实例化出来一个新的对象,对象和对象之间可能是不同的
"""
    不相同
    a1 = A()
    a2 = A()
    a1 != a2
    相同
    a1 = A()
    a2 = a1
    a1 == a2
"""
# 方法
"""
    不在类中声明 叫做函数
    在类中声明 就叫方法
"""
# 内置方法
"""
    在类中存在一些特殊的方法,这些方法使用__开头,__结尾
    最具有代表性的方法就是 __init__(self) 方法
    所有方法中 self参数在调用时 不需要传值
    self表示 谁调用这个方法 self就代表谁
    此方法 一定会在实例化对象时自动调用
    此方法 通常用来初始化对象
    初始化即为给变量赋初始值
"""
# 实例方法
"""
    没有装饰器修饰的 括号中有self的 都是实例方法
    实例方法 必须有 对象的调用才能使用
    但是在同一个类中 方法和方法之间是可以互相调用的
    例如:
    class A:
        def a(self):
            pass
        def b(self):
            a()
"""
# 类方法
"""
    即 使用@classmethod装饰器修饰的方法
    只和类相关
    括号中是cls
    class A:
        @classmethod
        def a(cls):
            pass
"""
# 静态方法
"""
    使用@staticmethod装饰器修饰的方法
    括号中没有cls 和 self
"""
# 继承
"""
    面向对象的特点
    子类可以继承父类中的属性和方法
    python允许多继承
    class father(object):
        a = 10
        def b(self):
            return "pass"
    class son(father):
        pass
    
    s = son()
    print(s.a) => 10
    print(s.b()) => pass
"""
# 重写
"""
    子类可以继承父类中的属性和方法
    如果父类的需求不满足子类的需要
    子类就可以重写父类方法,以满足自己需要
    class father(object):
        a = 10
        def b(self):
            return "pass"
    class son(father):
        def b(self):
            return "bbbb"
    
    s = son()
    print(s.a) => 10
    print(s.b()) => bbbb
"""
# 多态
"""
    父类类型代表子类对象
    class Animal():
        def run(self):
            print('动物跑')
    
    class Dog(Animal):
        def run(self):
            print('狗跑')
    
    class QQ(Animal):
        def run(self):
            print('企鹅游泳')
    
    class Bird(Animal):
        def run(self):
            print('鸟飞')
            
    # 鸭子类型
    # 只要一个东西 长得像鸭子 叫声也像鸭子 走起来像鸭子 它就是鸭子
    
    def testRun(a):
        a.run()
    
    testRun(Animal()) => 动物跑
    testRun(Dog()) => 狗刨
    testRun(QQ()) => 企鹅游泳
    testRun(Bird()) => 鸟飞
"""