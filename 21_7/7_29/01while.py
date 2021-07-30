# 开发时间:  2021/7/29 8:04
# name = input("please enter your name:")
# print(f"\nHello, {name}")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
