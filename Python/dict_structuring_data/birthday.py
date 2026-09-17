# birthdays = {
#     'Kofi': 'July 7',
#     'Kin':  'March 15',
#     'Ama':  'June 3',
#     'Carol': 'March 4',
#     'Alice': 'Apr 1'
# }

# while True:
#     print('Enter a name: ()')
#     name = input()
#     if name == '':
#         break


#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

#Returning Keys and Values
# spam = {'color': 'red', 'age':42}
# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# for i in spam.items():
#     print(i)


# spam1 = {'name': 'Pooka', 'age':5}
# if 'color' not in spam1:
#     spam1['color'] = 'black'
# print(spam1)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1 

print(count)   