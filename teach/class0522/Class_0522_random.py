import random

# 随机数 [0, 1)
print(random.random())

# 随机整数 [1, 10]
print(random.randint(1, 10))

# 随机浮点数 [0.1, 0.2]
print(random.uniform(0.1, 0.2))

# 从序列(元组 列表 集合)中抽样
li = list(range(100))
print(random.sample(li, 10))

#
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))

# 从序列中返回一个数
print(random.choice(li))

# 乱序
print(random.shuffle(li))
print(li)
