# 开发时间:  2021/7/30 19:57
lst = [10, 20, 30]
print(id(lst))
lst.append(40)
print(id(lst))

s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
