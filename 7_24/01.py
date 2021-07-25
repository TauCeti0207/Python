# 开发时间:  2021/7/24 14:49
print(1+1)
print(1-1)
print(1*2)
print(1/2)
print(11//2)    # 整除运算
print(11/2)
print(11 % 2)
print(2**3)

print(-9//-2)
print(-9//4)
print(9//-4)    # 向下取整
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(a, type(a))
a /= 3
print(a)
print(a, type(a))
a = b = c = 20
a %= 3
print(a, type(a))

a, b, c = 20, 30, 40
print(a, id(a))
print(b, id(b))
# print(c, id(c))

# 交换
a, b = b, a
print(a, id(a))
print(b, id(b))

print(a > b)
print(a == b)
print(a != b)
print(a is b)   # 判断a,b的id标识是否相等
print(a is not b)

a = 10
b = 10
print(a != b)
print(a is b)

print(a == 1 and b <= 10)
print(a == 1 or b <= 10)
print(not a)
c = 0
print(not c)

s = 'hello world'
print('w' in s)
print('w' not in s)
print(bin(4))
print(bin(8))
print(4 & 8)
print(4 | 8)
print(bin(4 | 8))

print(4 << 1)
print(4 << 2)
print(4 >> 1)
print(4 >> 2)
print(4 >> 3)

print(bool(False))
print(bool(0))
print(bool(0.01))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))
print(bool(()))
print(bool(tuple()))
print(bool(set()))


print(bool(True))


money = 1000
s = int(input('请输入取款金额'))
if money >= s:
    money = money - s
    print('取款成功,余额为', money)
else:
    print("没钱啦")
