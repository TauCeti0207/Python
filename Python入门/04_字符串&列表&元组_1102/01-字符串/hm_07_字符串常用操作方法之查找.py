mystr = "hello world and itcast and itheima and Python"

# 1. find() 找到了返回下标，找不到返回-1
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # -1 , ands子串不存在


# 2.index() 找到了返回下标，找不到报错
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
# print(mystr.index('ands'))  # 如果index查找子串不存在，报错

# 3.count() 返回的字串出现次数
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('and'))  # 3
print(mystr.count('ands'))  # 0


# 4.rfind() 和find相同，从右侧开始查找
print(mystr.rfind('and'))  # 35 找到的最后一个and
print(mystr.rfind('ands'))

# 5.rindex()
print(mystr.rindex('and'))  # 35
print(mystr.rindex('ands'))  # 报错 ValueError: substring not found