with open('demo.txt', 'r', encoding="utf-8") as f:
    # f.close()
    print(f.name)
    # 读取所有
    c = f.read()
    print(c)
print("-" * 100)
with open('demo.txt', 'r', encoding="utf-8") as f:
    # f.close()
    print(f.name)
    # 去除空格
    # 读取一行
    print(f.readline().strip())
    print(f.readline())
    print(f.readline())
    print(f.readline())
print("-" * 100)
with open('demo.txt', 'r', encoding="utf-8") as f:
    # f.close()
    print(f.name)
    # 读取所有行 返回列表
    print(f.readlines())