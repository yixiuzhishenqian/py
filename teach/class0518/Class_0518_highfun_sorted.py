# 将函数作为参数使用的函数就是高阶函数
# sorted

# reverse 倒序
print(sorted(list(range(20)), reverse=True))
# key 设置排序规则
li1 = [5, -1, 3, 6, -7, 8, -11, 2]
print(sorted(li1, key=abs))

print(sorted(li1, key=lambda x: x ** 2, reverse=True))
