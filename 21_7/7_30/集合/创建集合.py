# 开发时间:  2021/7/30 20:21
s = {1, 2, 2, 4, 5, 5, }
print(s)

s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 2, 2, 3, 3, 4, 5, 5,])
print(s2, type(s2))

s3 = set((1, 2, 2, 3, 4, 5, 76,))
print(s3, type(s3))

s4 = set('python')
print(s4, type(s4))

s5 = set()
print(s5, type(s5))
