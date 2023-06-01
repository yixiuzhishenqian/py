# tupple 元组 ()
# +-*/
# */ (+-
# 只有一个元素的时候,需要在元素后面加上 逗号
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(tup))
print(tup)

print(tup[0:2])
# tup[0] = '一' 此操作为非法操作,元组中的元素不支持更改(新增/插入/修改/删除)
tup1 = (10, 11)
# 链接元组
tup2 = tup + tup1
print(tup2)
print(len(tup * 3))
# 查看元组中是否包含某个元素 in
print(10 not in tup)

# 字符串 元组 列表可以互相转换
str1 = '123456789'
tup3 = tuple(str1)
tup4 = tuple([1, 2, 3, 4, 5])
li = list(tup4)
print(type(str(li)))


