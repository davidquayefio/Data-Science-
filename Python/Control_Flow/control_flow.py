# username = 'David'
# password = '1234year'

# if username == 'David':
#     print('Hello David')
#     if password == '1234year':
#         print('Password correct')
#     else:
#         print('Password incorrect')

name = 'Alice'
if name == 'Alice':
    print('Hi Alice')

name = 'Bob'
if name == 'Bob':
    print('Hi Bob')
else:
    print('Hello stranger.')

name = 'Charlie'
if name == 'Bob':
    print('Hi Charlie') 
else:
    print('Hello stranger.')

name = 'Charlie'
age = 23
if name == 'Charlie':
    if age < 12:
        print('You are not allowed to enter')
    else:
        print('Welcome Charlie')

name = 'Carol'
age = 150
if name == 'Carol':
    print('Hi Carol')

elif age < 12:
    print('You are not allowed to enter.')

elif age > 120:
    print('Unrealistic age. Please try again.')

elif age < 120:
    print('Welcome Carol')


name = 'David'
age = 3000

if name == 'David':
    print('Hi David')
elif age < 12:
    print('You are not allowed to enter.')
elif age > 120:
    print('Unrealistic age. Please try again.')

elif  age > 2000:
    print('You are a time traveler! Welcome David')

name = 'Eve'
age = 38383

if name == 'Eve':
    print('Hi Eve')
elif age < 12:
    print('You are not allowed to enter.')  
else:print('You are neither a Eve nor a child. Please try again.')