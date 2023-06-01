se1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, '1'}
se2 = set(['1', '2', '3', '4'])

print(se1)
print(se2)

se3 = set()

# 添加元素
se3.add(123)
print(se3)
se3.update((1, 2, 3))
print(se3)
se3.update(['one', 'two', 'three'])
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
print(se3.update(dic))

print(se3)
print(se3.remove('name'))
print(se3.discard('name'))
print(se3.pop())
print(se3)
