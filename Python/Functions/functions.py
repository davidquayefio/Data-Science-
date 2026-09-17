# def hello():
#     print("Hello, good morning!")
#     print("Hello, good afternoon!")
#     print("Hello, good evening!")

# hello()
# hello()
# hello()
# hello('John')
# hello()

#Arguents and Parameters
# def say_hello(name):
#     print('Hello, ' + name + '!')
#     print('How are you doing?')
#     print('Have a great day!')

# say_hello('Alice')

from math import factorial
import random
# def get_answer(answer_number):
    # if answer_number == 1:
    #     return 'It is certain'
    # elif answer_number == 2:
    #     return 'It is decidedly so'
    # elif answer_number == 3:
    #     return 'Yes'
    # elif answer_number == 4:
    #     return 'Reply hazy try again'
    # elif answer_number == 5:
    #     return 'Ask again later'
    # elif answer_number == 6:
    #     return 'Concentrate and ask again'
    # elif answer_number == 7:
    #     return 'My reply is no'
    # elif answer_number == 8:
    #     return 'Outlook not so good'
    # elif answer_number == 9:
    #     return 'Very doubtful'

# print('Ask a yes or no question:')
# input('>')
# r = random.randint(1, 9)
# print(get_answer(r))

# for i in range(100):
#     if random.randint(0, 1) == 0:
#         print('H', end='')
#     else:
#         print('T', end=' ')
# print()

# def factorial(n):
#     """return n!"""
#     return 1 if n < 2 else n * factorial(n - 1)
# print(factorial(42))

import math 
factorial.__doc__

fact = factorial 
print(fact(5))

print(factorial, range(12))

print(list(map(factorial, range(12))))