# list 列表 -
# 创建列表
ll = [1, 2, [3, 4, 5], None, False, 1, '9', '0']
# 内置方法
li = list(range(1, 11))
print(li)
# 列表的长度
print(len(li))
print(len(ll))
# 元素出现的次数
print(li.count(1))
print(ll.count(1))
# 最大值 / 最小值
print(max(li))
print(min(li))
# print(max(ll))

# 追加新元素
li.append(11)
print(li)
# 追加多个
li2 = [12, 13, 14]
li.extend(li2)
print(li)
# index
print(li.index(12))
# 插入
li.insert(5, '五')
print(li)
# 默认移除最后一个
# 有参数移除索引所在位置的元素
li.pop(0)
print(li)
# remove 移除第一个匹配的元素
li.remove('五')
print(li)
# 反转
# li.reverse()
# print(li)
# 排序
# li.sort()
# print(li)
li.sort(reverse=True)
print(li)
# 复制
li2 = li.copy()
# 清空
li.clear()
print(len(li))
print(li2)
# 元素赋值
li2[4] = '拾'
print(li2)
# 使用del删除元素
del li2[4]
print(li2)