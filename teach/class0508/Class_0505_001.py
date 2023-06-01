# # 切片
# # 0 开始下标
# # 2 长度
# print(string[0:2])
# print(string[4])
# # fedcba
# # gafedc
# print(string[5:0:-1])
# # 负数表示从后往前
# print(string[-1])
# # 不写长度,意为到最后
# print(string[3:])


# 查找 find index
# print(string.find('a'))
# print(string.find('c'))
# print(string.find('z'))
# print(string.index('a'))
# print(string.index('c'))
# 找不到会报错,抛出异常 ValueError: substring not found
# print(string.index('z'))
# rfind rindex
# print(string.rfind('a'))
# print(string.rfind('c'))
# print(string.rfind('z'))
# print(string.rindex('a'))
# print(string.rindex('c'))
# 找不到会报错,抛出异常 ValueError: substring not found
# print(string.rindex('z'))


# print(string.upper())
# print(string.upper().lower())
# # 大小写互换
# print(string.swapcase())
# # 首字母大写
# print(string.capitalize())
# # 首字母大写的字符串 为True
# print(string.istitle())
# print(string.isupper())
# print(string.islower())

string = '   Abcdefag   '
# print(string)
# print(string.strip())
# print(string.lstrip())
# print(string.rstrip())

# string1 = '%s %s %s' % ('安东', '你好', 99)
# print(string1)
# name = '张三'
# sex = '男'
# age = 56
# string2 = f'{name}{sex}{age}'
# print(string2)

li = ['1', '2', '3', '7', '8', '9']
string3 = '-'.join(li)
print(string3)
l = string3.split("-")
print(l)
