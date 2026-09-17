fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

def reverse(word):
    return word[::-1]
print(reverse('testing'))

print(sorted(fruits, key=reverse))

from math import factorial

print(list(map(factorial, range(6) ))) #It will build list of factorials from 0! to 5!

print(list(map(factorial, filter(lambda n: n % 2, range(10))))) #odd numbers up to 5!
# Or 
print([factorial(n) for n in range(10) if n % 2])

from functools import reduce
from operator import add
print(reduce (add, range(100)))

import random 

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

metro_data = [
    
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
 ]

from operator import itemgetter
for city in sorted (metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

from collections import namedtuple
LatLon = namedtuple ('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
               for name, cc, pop, (lat, lon) in metro_data]

print(metro_areas[0])

print(metro_areas[0].coord.lat)

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key = attrgetter('coord.lat')):
    print(name_lat(city))

import time, sys
# indent = 0  # How many spaces to indent
# indent_increasing = True  # Whether the indentation is increasing or not

# try:
#     while True:  # The main program loop
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10th of a second.

#         if indent_increasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indent_increasing = False
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indent_increasing = True
# except KeyboardInterrupt:
#     sys.exit()

"""
Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.

Then, write a program that lets the user enter an integer 
and that keeps calling collatz() on that number until the 
function returns the value 1. (Amazingly enough, this sequence actually works for any integer;
 sooner or later, using this sequence, you’ll arrive at 1! 
Even mathematicians aren’t sure why. Your program is exploring what’s called 
the Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() 
to an integer with the int() function; 
otherwise, it will be a string value. To make the 
output more compact, the print() calls that print the numbers
 should have a sep=' ' named parameter to print all values on one line.

"""


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result, end=' ')
    return result


number = int(input('Enter an integer: '))
print(number, end=' ')
while number != 1:
    number = collatz(number)