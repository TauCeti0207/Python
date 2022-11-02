# 三角形： 每行星星的个数和行号数相等
j = 0
while j < 5:
    # 一行星星开始
    i = 0
    while i < j + 1:  # 等价while i <= j:
        print('*', end='')
        i += 1
    # 一行星星结束：换行显示下一行
    print()  # print默认带有\n
    j += 1
