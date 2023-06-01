# 键必须是不可变类型 str int tuple
dic = {
    "name": "anton",
    "age": 34,
    "sex": "男",
    "tup": (1, 2, 3),
    "li": [4, 5, 6],
    (1, 2): {
        "k1": "v1",
        "k2": "v2"
    }
}
# 根据键获取字典中对应的值
print(dic.get('name'))
print(dic['name'])
# print(dic.name)

print(dic[(1, 2)].get('k1'))

# 修改值
# dic.update(key='sex', value='女')
dic['sex'] = '女'
print(dic)
# keyError 键错误
# print(dic['aaa'])

# 添加键值对
dic['phoneNum'] = 13311097871
print(dic)
# 删除字典元素
del dic['phoneNum']
print(dic)

print(type(str(dic)))

dic2 = dic
dic3 = dic.copy()
dic['phoneNum'] = 13311097871
print(dic2)
print(dic3)

#
print("&"*88)
dic4 = dic.fromkeys([1, 2, 3, 4, 5])
print(dic4)
# keys 获取所有键
print(list(dic4.keys()))

seq = ('name', 'age', 'class')
dic5 = dic.fromkeys(seq, ('zs', 55, '1ban'))
print(dic5)

# 判断字典中是否包含指定的键
print('name1' not in dic)

print(list(dic.items())[0][0])
print("-" * 60)
# 设置默认值,有就返回,没有插入,插入的值是None
print(dic.setdefault('age'))
print(dic)
print(dic.setdefault('idcard'))
print(dic)

# 将一个字典中的所有键值对 更新到另一个字典中
dic.update(dic5)
print(dic)
# 获取所有值
print(list(dic.values()))

# 根据键删除键值对
print(dic.pop('name', '键未找到'))
print('name' in dic)
# 后进先出
print(dic.popitem())
print(dic)
print('age' in dic)
