# 分支结构
age = int(input("请输入您的年龄"))
# 1. 单一if
# if age >= 18:
#     print("已成年")
#     print('上网')
# 2. if else
# if age >= 18:
#     print("已成年")
#     print('上网')
# else:
#     print('未成年')
# 3. if elif ... elif else
if age > 0 and age <= 17:
    print('幼儿 青少年')
elif age > 0 and age <= 17:
    print('青年')
elif age >= 30 and age < 60:
    print('中年')
else:
    print('输入有误')
print("执行结束")