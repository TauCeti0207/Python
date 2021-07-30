# 开发时间:  2021/7/30 20:13
t = (10, [20, 30], 40)
print(t)
print(t[0], id(t[0]))
print(t[1], id(t[1]))
print(t[2], id(t[2]))

print(id(100))
t[1].append(100)
print(t[1], id(t[1]))