import json

# # 把json => str
# d = {'小明': {'sex': '男', 'addr': '上海', 'age': 26}, '小红': {'sex': '女', 'addr': '上海', 'age': 24}, }
# print(type(d))
# print(d)
# s = json.dumps(d, ensure_ascii=False, indent=2)
# print(type(s))
# print(s)
# f = open("d:/myjson.json", 'w', encoding='utf-8')
# json.dump(d, fp=f, ensure_ascii=False, indent=4)

# # 把str => json
s = open("d:/myjson.json", 'r', encoding='utf-8')
# o = json.loads(s.read())
# print(o)
# print(type(o))
print(json.load(s))