# 开发时间:  2021/7/23 15:11
#输出字符串单引号双引号都行
print('hello world')
print("hello world")
print(52013114)
fp=open('D:/test.txt','a+')
print('hello world',file=fp)  #a+文件如果不存在就创建,如果存在就在文件后面内容进行修改
fp.close()

#不换行输出
print('hello','world','python')