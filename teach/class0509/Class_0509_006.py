# continue
# 打印 1 - 100 之间的所有能被3整除的数
# num = 1
# while num <= 100:
#     if num % 3 == 0:
#         print(num)
#     num += 1

# continue版
# num = 1
# while num <= 100:
#     num += 1
#     if num % 3 != 0:
#         continue
#     print(num)


# break 中断
# 一个乞丐,天桥卖艺,第一天要2元,第二天是前一天的两倍
# 问 要够10240元需要多少天
day = 1
total = 0
money = 2
while True:
    if total >= 10240:
        break
    money *= 2
    total += money
    day += 1
print(total)
print(day)
print(money)
# 从1开始累加 到5050结束循环
# num = 1
# sum = 0
# while True:
#     sum += num
#     num += 1
#     if sum == 5050:
#         break
# print(num)
# print(sum)
