# 开发时间:  2021/7/28 7:04
bicycles = ['trek', 'cannonade', 'radian', 'specialize']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
message = f"My friend bicycle was a {bicycles[0].title()}."
print(message)
bicycles[0] = 'track'
print(bicycles)
bicycles.append('trek')
print(bicycles)
bicycles.insert(0, 'ducat')
print(bicycles)
del bicycles[0]
print(bicycles)


popped_bicycles = bicycles.pop(1)

print(bicycles)
print(popped_bicycles)
message1 = f"The last bicycle I owned was a {popped_bicycles.title()}."
print(message1)


print(bicycles)
bicycles.remove('track')
print(bicycles)
too_expensive = 'track'
print(f"\nA {too_expensive.title()} is too expensive for me.")


