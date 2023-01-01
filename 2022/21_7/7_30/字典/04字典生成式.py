# 开发时间:  2021/7/30 19:22
items = ['Fruits',
         'Books',
         'Others', ]
prices = [98, 99, 87]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
