dic1 = {1, 2, 3, 4, 5, 6}

dic2 = {1, 3, 5, 7, 9, 11}
# 差集 {2,4,6}
dic3 = dic1 - dic2
print(dic3)
# 并集 去除重复 {1,2,3,4,5,6,7,9,11}
dic4 = dic1 | dic2
print(dic4)
# 交集 {1,3,5}
dic5 = dic1 & dic2
print(dic5)
# 补集 {2,4,6,7,9,11}
dic6 = dic1 ^ dic2
print(dic6)

a = {x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x > 2}
print(a)

# 差集 -
# dic7 = dic1.difference(dic2)
# print(dic3)
# print(dic7)
#
# dic1.difference_update(dic2)
# print(dic1)

# 交集 &
# dic8 = dic1.intersection(dic2)
# print(dic8)
# print(dic5)
#
# dic1.intersection_update(dic2)
# print(dic1)

# 并集 |
# dic9 = dic1.union(dic2)
# print(dic9)
# print(dic4)

print(dic1.isdisjoint(dic2))
# 5是1的子集吗
print(dic5.issubset(dic1))
# 1是5的父级吗 超级
print(dic1.issuperset(dic5))

# 补集 ^
# dic10 = dic1.symmetric_difference(dic2)
# print(dic6)
# print(dic10)
#
# dic1.symmetric_difference_update(dic2)
# print(dic1)