mystr = "hello world and itcast and itheima and Python"

# 1. startswith(字串，开始位置下标，结束位置下标): 判断字符串是否以某个子串开头
print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('helo'))


# 2. endswith(): 判断字符串是否以某个子串结尾
print(mystr.endswith('Python'))
print(mystr.endswith('thon'))
print(mystr.endswith('Pythons'))


# 3. isalpha(): 所有字符都是字母返回True
print("isalpha:", end=' ')
print(mystr.isalpha())

# 4. isdigit(): 所有字符都是数字返回True
print(mystr.isdigit())

mystr1 = '12345'
print(mystr1.isdigit())

# 5. isalnum() : 所有字符都是数字或者字符返回True
print(mystr1.isalnum())  # True
print(mystr.isalnum())  # False
mystr2 = 'abc123'
print(mystr2.isalnum())


# 6.isspace(): 所有字符都是空白返回True
print(mystr.isspace())
mystr3 = '   '
print(mystr3.isspace())

