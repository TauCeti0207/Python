# 开发时间:  2021/7/30 20:28
s = {10, 20, 30, 40, }
print(10 in s)
print(20 not in s)

s.add(100)
print(s)

s.update({200, 499, 399, })
print(s)

s.remove(100)
print(s)

s.discard(209)
print(s)

s.pop()
print(s)

s.clear()
print(s)
