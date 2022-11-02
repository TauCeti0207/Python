mystr = "hello world and itcast and itheima and Python"

# 1. replace() 把and换成he  replace函数有返回值，返回值是修改后的字符串
new_str = mystr.replace('and', 'he')  # 默认是-1 替换所有的子串
# new_str = mystr.replace('and', 'he', 1)
# 替换次数如果超出子串出现的次数，表示替换所有这个子串
# new_str = mystr.replace('and', 'he', 10)
print(mystr)
print(new_str)

# ***** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# --- 说明 字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型


# 2. split(str, num) -- 分割，返回一个列表 num表示分割字符出现的次数，将来返回的数据个数位num+1
# 分割字符不再出现
list1 = mystr.split('and')
list1 = mystr.split('and', 2)
print(list1)
print(type(list1))


# 3. join() -- 合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
#
# aa...bb...cc
new_str1 = '...'.join(mylist)  # aa...bb...cc
print(new_str)

new_str2 = '...'.join(mylist[0])  # a...a
print(new_str2)
