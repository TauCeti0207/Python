# 开发时间:  2021/7/24 16:58
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}")

message = f"hello, {full_name.title()}!"
print(message)

print("\tPython")

favorite_language = '  ace   '
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = '  ace   '
print(favorite_language)
favorite_language = favorite_language.rstrip()  # delete right blank space
print(favorite_language)
favorite_language = '  ace   '
print(favorite_language)
favorite_language = favorite_language.strip()   # delete all blank space
print(favorite_language)

message1 = 'Hello Eric, would you like to learn some Python today'
print(message1)

name1 = 'zhang san'
print(name1.title())
print(name1.lower())
print(name1.upper())

message2 = 'Albert Einstein once said,"A person who never made a mistake never tried anything new."'
print(message2)


famous_person = 'Albert Einstein'
saying = ' once said,"A person who never made a mistake never tried anything new."'
message3 = famous_person + saying
print(message3)

person_name = '   li \n\tsi'
print(person_name)
person_name = person_name.lstrip()
print(person_name)
person_name = '   li \n\tsi'
print(person_name)
person_name = person_name.rstrip()
print(person_name)
person_name = '   li \n\tsi'
print(person_name)
person_name = person_name.strip()
print(person_name)


universe_age = 12_000_000_000_000
print(universe_age)

number = 7
message4 = 'my favorite number is ' + str(number)
print(message4)
