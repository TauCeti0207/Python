# 开发时间:  2021/7/28 7:13
names = ['Baker', 'Jesse', 'Jimmy']
print("Hi " + names[0])
print("Hi " + names[1])
print("Hi " + names[2])

communicate = ['Honda motorcycle', 'car']
message = f"I would like to own a {communicate[0]}."
print(message)
print()


print('练习3-4')
invite = ['yuanchao', 'liming', 'Danny']
print("I want invite" + ' ' + invite[0] + ',' + invite[1] + ',' + invite[2] + ' ' + "have supper")
print(invite[1] + "Can't go")
invite[1] = 'july'
print("I want invite" + ' ' + invite[0] + ',' + invite[1] + ',' + invite[2] + ' ' + "have supper")
print("Now I find a big table")
invite.insert(0, 'wukong')
invite.insert(2, 'baijiu')
invite.append('shashen')
print("I want invite" + ' ' + invite[0] + ',' + invite[1] + ',' + invite[2] + ',' + invite[3] + ',' + invite[4] + ',' + invite[5] + ' ' + "have supper")
print("Now only can I invite two person")
person = invite.pop()
print("Sorry "+person+" I can't invite you !")
person = invite.pop()
print("Sorry "+person+" I can't invite you !")
person = invite.pop()
print("Sorry "+person+" I can't invite you !")
person = invite.pop()
print("Sorry "+person+" I can't invite you !")
print(invite[0]+" I will invite you ")
print(invite[1]+" I will invite you ")
del invite[1]
del invite[0]
print(invite)

print('------3__8------')
place = ['a', 'e', 'b', 'c', 'd']
print(place)
print(sorted(place))
print(place)
place.sort(reverse=False)
print(place)
