# 开发时间:  2021/7/30 20:34
s1 = {10, 20, 30, 40}
s2 = {40, 30, 20, 10}
print(s1 == s2)
print(s1 != s2)

s3 = {10, 20, 30, 40, 50, 60}
s4 = {10, 20, 30, 40}
s5 = {10, 20, 50, 90}
print(s4.issubset(s3))
print(s5.issubset(s3))
print(s3.issuperset(s4))
print(s3.issuperset(s5))

print(s4.isdisjoint(s5))
print(s4.isdisjoint(s3))
