# 开发时间:  2021/7/24 16:15
score = int(input('请输入一个成绩:'))
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('error')
