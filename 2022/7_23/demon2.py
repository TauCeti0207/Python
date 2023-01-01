# 开发时间:  2021/7/23 15:52
print(chr(0b100111001011000))
print(ord('乘'))
# 20056是100111001011000对应的十进制
import keyword
print(keyword.kwlist)
name = '玛丽亚'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
name = '楚留香'
print(name)
n1 = 90
n2 = -90
n3 = 0
print(n1, n2, n3, type(n1), type(n2))
# python默认为十进制
print('二进制', 0b10101111)
print(10101111)
print('八进制对应十进制', 0o176)
print('十六进制', 0x1eaf)
n1 = 1.1
n2 = 2.2
print(n1+n2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
f1 = True
print(f1+1)
# bool可以转成整数
print(False+2)
# True,False要首字母大写!!!

str1 = '人生苦短,我用python'
str2 = "人生苦短,我用python"
str3 = '''人生苦短,
我用python'''
str4 = """人生苦短,
我用python"""
print(str1)
print(str2)
print(str3)
print(str4)
# 三引号可以多行显示

name = '张三'
age = 20
print('我叫'+name+',今年'+str(age)+'岁')
# 类型转换,连接才不报错
s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(int(s1), type(int(s1)))    # 数字串可以转
print(int(f1), type(int(f1)))    # float可以转
# print(int(s2), type(int(s2)))     小数串不能转
print(int(ff), type(int(ff)))
# print(int(s3), type(int(s3)))     字符串不能转


# port this
"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

"""
'''
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
'''
i = 98
print(float(i), type(float(i)))
a = int(input('a = '))
b = int(input('b = '))
# str类型要转换成int才能进行运算,否则只是连接
print(a+b)
