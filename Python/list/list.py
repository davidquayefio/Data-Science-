list_strings = ['cat', 'bat', 'rat', 'elephant']
print(list_strings)

print(list_strings[0])
print(list_strings[1])
print(list_strings[2])
print(list_strings[3])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][0])
print(spam[1][3])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

# cat_name_1 = 'Zophie'
# cat_name_2 = 'Pooka'
# cat_name_3 = 'Simon'
# cat_name_4 = 'Lady Macbeth'

# print('Enter the name of cat 1:')
# cat_name_1 = input()
# print('Enter the name of cat 2:')
# cat_name_2 = input()
# print('Enter the name of cat 3:')
# cat_name_3 = input()
# print('Enter the name of cat 4:')
# cat_name_4 = input()
# print('The cat names are:')
# print(cat_name_1 + ' ' + cat_name_2 + ' ' + cat_name_3 + ' ' + cat_name_4)

cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # List concatenation
print('The cat names are:')
for name in cat_names:
    print('  ' + name)

for i in range(10):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])