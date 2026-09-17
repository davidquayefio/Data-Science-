# spam = 0 
# if spam < 5: 
#     print('Hello, world.') 
#     spam = spam + 1

# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input('>')
#     if name == 'your name':
#         break
# print('Thank you!')

# while True:
#     print('Who are you?')
#     name = input('>')
#     if name != 'David':
#         continue
#     print('Hello, David. What is the password? (It is a fish.)')
#     password = input('>')
#     if password == 'swordfish':
#         break
# print('Access granted.')
# 
# print('hello')
# for i in range(5):
#     print('On this iteration, i is ' + str(i))
# print('Done.')

# print('Hello, world!')
# i  = 0
# while i < 5:
#     print('On this iteration, i is ' + str(i))
#     i = i + 1
# print('Done.')

# for i in range(12, 17):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# import random
# for i in range(5):
#     print(random.randint(1, 10))

# import sys

# while True:
#     print('Type exit to exit.')
#     response = input('>')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0  
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (rock, paper, scissors)')
        playerMove = input('>')
        if playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissors':
            break
        print('Type one of rock, paper, scissors.')

    if playerMove == 'rock':
        print('ROCK versus...') 
    elif playerMove == 'paper':
        print('PAPER versus...')
    elif playerMove == 'scissors':
        print('SCISSORS versus...')

    randomNumber = random.randint(0, 2)
    if randomNumber == 0:
        computerMove = 'rock'
        print('ROCK')
    elif randomNumber == 1:
        computerMove = 'paper'
        print('PAPER')
    elif randomNumber == 2:
        computerMove = 'scissors'
        print('SCISSORS')   

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'rock' and computerMove == 'scissors':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'paper' and computerMove == 'rock':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'scissors' and computerMove == 'paper':
        print('You win!')
        wins = wins + 1
    else:
        print('You lose!')
        losses = losses + 1 