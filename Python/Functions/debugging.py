# def box_print(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')

#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)

# try:
#     box_print('*', 15, 5)
#     box_print('O', 20, 10)
#     box_print('**', 15, 5)
# except Exception as err:
#     print('An exception happened: ' + str(err))
# try:
#     box_print('O', 1, 3)
# except Exception as err:
#     print('An exception happened: ' + str(err))


# ages = [22, 55, 62, 45, 21, 22, 34, 42]


# def remove_older_than_50(age):
#     if age > 50:
#         raise ValueError('Age is over 50')
#     return age


# try:
#     younger_ages = [
#         remove_older_than_50(age)
#         for age in ages
#         if age <= 50
#     ]
#     print(younger_ages)
# except ValueError as err:
#     print('A value error happened: ' + str(err))


# ages = [26, 57, 92, 54, 22, 15, 17, 11, 47]

# ages.sort()
# print(ages)

# assert ages[0] <= ages[-1], \
#     'First age is not less than or equal to last age'



# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

import logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')

def factorial(n):
    logging.debug('Start of factirial(' + str(n) + ')')
    total=1
    for i in range(n + 1):
            total *= 1
            logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')

print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)

import random
heads = 1

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
            heads = heads + 1
    if i == 500:
          print('Halfway done!')
print('Heads came up ' + str(heads) + 'times.')