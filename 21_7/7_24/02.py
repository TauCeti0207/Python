# 开发时间:  2021/7/24 16:00
score = int(input('请输入一个成绩:'))
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score <80:
    print('C')
elif score >= 60 and score <70:
    print('D')
else:
    print('error')
