# 开发时间:  2021/7/28 8:37
cars = ['bwn', 'audi', 'typto', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.sort(reverse=False)
print(cars)
cars = ['bwn', 'audi', 'typto', 'subaru']
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))
print('\n')
cars = ['bwn', 'audi', 'typto', 'subaru']
for car in cars:
    print(car)
    print(f"{car.title()}, that was a great car!\n")
print("thank you everyone")
print("\n")

for value in range(1,5):
    print(value)

number = list(range(1,6))
print(number)

number1 = list(range(2, 11, 2))
print(number1)

squares = []
for value1 in range(1,11):
    squares.append(value1**3)
print(squares)

print("\n")

digits = [1, 2, 3, 4, 5, 2, 5, 22, 55]
print(min(digits))
print(max(digits))
print(sum(digits))

squares1 = [value2**3 for value2 in range(1, 11)]
print(squares1)

for value3 in range(1, 21):
    print(value3)
print('\n')

print()

for value4 in range(3, 31, 3):
    print(value4)

cars = ['bwn', 'audi', 'typto', 'subaru']
print(cars[1:4])
print(cars[:4])
print(cars[-3:])

for car in cars[:3]:
    print(car.title())

my_friend_cars = cars[:]
print(my_friend_cars)

pizzas = ['beef pizza', 'seafood pizza', 'super pizza']
friend_pizzas = pizzas[:]
pizzas.append('cheese pizza')
friend_pizzas.append('garden pizza')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)