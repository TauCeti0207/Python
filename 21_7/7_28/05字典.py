# 开发时间:  2021/7/28 19:31
languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = languages['sarah'].title()
print(f"Sarah's language is {language}")

alien_0 = {'color': 'green',
           'speed': 'slow'
           }
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
        }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
            }
for name in languages.keys():
    print(name.title())

languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
            }
for name in sorted(languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
            }
for language in set(languages.values()):
    print(language.title())

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow',
                 }
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow',
                 }
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
        }
print(pizza['crust'])
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
        'aeinstein': {
            'first': 'Albert',
            'last': 'Einstein',
            'location': 'Princeton',
                    },
        'mcurie': {
            'first': 'Marie',
            'last': 'Curie',
            'location': 'Paris',
        },
        }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(full_name)
    print(location)
