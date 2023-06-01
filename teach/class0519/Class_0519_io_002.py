with open("demo.txt", 'w') as f:
    # 先清空,再写入数据
    f.write('\n123456789')
print('-' * 30)
with open("demo.txt", 'a') as f:
    # 先清空,再写入数据
    f.write('\n987654321')
print('-' * 30)
with open("demo.txt", 'a') as f:
    # 先清空,再写入数据
    f.write('\n987654321')
print('-' * 30)